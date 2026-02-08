import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# =========================
# CONFIG
# =========================
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

# =========================
# DATA INGESTION
# =========================
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting Data Ingestion")

        try:
            # 1️⃣ Read dataset
            data_path = os.path.join("notebook", "data", "stud.csv")
            df = pd.read_csv(data_path)
            logging.info("Dataset loaded successfully")

            # 2️⃣ Create artifacts folder
            os.makedirs("artifacts", exist_ok=True)

            # 3️⃣ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            # 4️⃣ Split data
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # 5️⃣ Save train & test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data Ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
