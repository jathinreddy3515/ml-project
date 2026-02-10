# 📊 Student Performance Prediction — End-to-End ML Project

This project is an **end-to-end machine learning application** that predicts a student's math score based on demographic and academic features.  
It covers **data collection, preprocessing, model training, a web interface, and deployment on Azure App Service**.

---

## 🌟 Live Demo

[Click here to access the live app](https://student-performance-ml-predictor-jathin-dseehpf8aef9d2dm.centralindia-01.azurewebsites.net/predictdata)

---

## 📖  What This Project Does

While studying, I became fascinated by how **data can reveal hidden patterns and help make predictions**.  
This curiosity led me to learn **data analysis and machine learning**, and to build this project step by step:

1. Started with raw student data.  
2. Trained a predictive model.  
3. Built a Flask web application.  
4. Deployed the app on **Azure App Service**.  

**GitHub Actions** automatically updates the live application whenever changes are pushed to the main branch.

---

## 🧱 Project Structure

```text
ml-project/
│
├── app.py                  # Flask app entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py      # Load and split raw data
│   │   ├── data_transformation.py # Clean, encode, scale features
│   │   └── model_trainer.py       # Train and save ML model
│
│   ├── pipeline/
│   │   ├── train_pipeline.py      # End-to-end training pipeline
│   │   └── predict_pipeline.py    # End-to-end prediction pipeline
│
│   ├── exception.py               # Custom exception handling
│   └── logger.py                  # Logging configuration
│
├── templates/
│   ├── index.html                 # Landing page
│   └── home.html                  # Prediction form page
│
└── artifacts/
    ├── model.pkl                  # Saved ML model
    └── preprocessor.pkl           # Saved preprocessing pipeline

---

## 🔄 Project Workflow (Simple Explanation)


Raw Data
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Model Training
   ↓
Model Saved
   ↓
User Input (Web Form)
   ↓
Prediction Output


## ⚙️ How the System Works

1. Read and prepare data
2. Transform features
3. Train ML model
4. Save model and preprocessor
5. Load model in Flask app
6. Accept user input
7. Display prediction
```

---

## 🌐 Flask Web Routes

```text
/            → Home page
/predictdata → Prediction page
```

---

## ▶️ Run the Project Locally

```bash
git clone https://github.com/jathinreddy3515/ml-project.git
cd ml-project
pip install -r requirements.txt
python app.py
```
🌐 Once the server is running, open your browser and access:
```text
http://127.0.0.1:10000
http://127.0.0.1:10000/predictdata
```

---

## 🚀 Production Server

```bash
gunicorn app:application
```

---

## ⚙️ App Settings (Azure)

```text
SCM_DO_BUILD_DURING_DEPLOYMENT = true
PYTHON_VERSION = 3.10
WEBSITES_PORT = 8000
```

---

## ☁️ Deployment Workflow

```text
GitHub Repository
   ↓
GitHub Actions
   ↓
Azure App Service
   ↓
Public URL
```

---

## 📦 Model Artifacts

```text
model.pkl
preprocessor.pkl
```

---

## ✅ Key Highlights

```text
- End-to-end ML project
- Modular architecture
- Flask web application
- Azure cloud deployment
- Production-ready setup
```

---

## 📌 Use Cases

```text
- Student performance analysis
- Education analytics
- ML portfolio project
- Interview demonstration
```

---

## 👨‍💻 Author

```text
Jathin Reddy
GitHub: https://github.com/jathinreddy3515
```




