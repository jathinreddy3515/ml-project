import sys
import os
from dataclasses import dataclass

# Numerical and data handling libraries
import numpy as np
import pandas as pd

# Sklearn preprocessing tools
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Custom exception and logging
from src.exception import CustomException
from src.logger import logging

# Utility function to save objects
from src.utils import save_object


# =========================
# CONFIGURATION CLASS
# =========================
@dataclass
class DataTransformationConfig:
    """
    Stores configuration related to data transformation
    """
    # Path where the preprocessing object will be saved
    preprocessor_obj_file_path = os.path.join(
        "artifacts", "preprocessor.pkl"
    )


# =========================
# DATA TRANSFORMATION CLASS
# =========================
class DataTransformation:
    """
    Handles feature engineering and preprocessing logic
    """

    def __init__(self):
        # Initialize configuration
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Creates and returns a preprocessing pipeline
        for numerical and categorical features
        """
        try:
            # Define numerical and categorical columns
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # -------------------------
            # Numerical Pipeline
            # -------------------------
            # 1. Replace missing values with median
            # 2. Standardize values (mean=0, std=1)
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            # -------------------------
            # Categorical Pipeline
            # -------------------------
            # 1. Replace missing values with most frequent value
            # 2. Convert categories to numerical form using OneHotEncoding
            # 3. Scale encoded values (without centering)
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            # Log column information
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # -------------------------
            # Column Transformer
            # -------------------------
            # Applies different preprocessing pipelines
            # to numerical and categorical columns
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns),
                ]
            )

            return preprocessor

        except Exception as e:
            # Raise custom exception with system details
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        """
        Applies preprocessing to train and test datasets
        and saves the preprocessing object
        """
        try:
            # Read training and testing data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and test data loaded successfully")

            # Get preprocessing object
            preprocessing_obj = self.get_data_transformer_object()

            # Define target column
            target_column_name = "math_score"

            # Separate input features and target variable (train)
            input_feature_train_df = train_df.drop(
                columns=[target_column_name]
            )
            target_feature_train_df = train_df[target_column_name]

            # Separate input features and target variable (test)
            input_feature_test_df = test_df.drop(
                columns=[target_column_name]
            )
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                "Applying preprocessing on training and testing data"
            )

            # Fit preprocessing on training data and transform
            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )

            # Transform test data using the same preprocessing
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            # Combine transformed features with target variable
            train_arr = np.c_[
                input_feature_train_arr,
                np.array(target_feature_train_df),
            ]
            test_arr = np.c_[
                input_feature_test_arr,
                np.array(target_feature_test_df),
            ]

            # Save preprocessing object for future inference
            logging.info("Saving preprocessing object")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj,
            )

            # Return processed arrays and preprocessor path
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            # Raise custom exception if any error occurs
            raise CustomException(e, sys)
