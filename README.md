# ⚖️ AutoJudge – Programming Problem Difficulty Predictor

AutoJudge is a machine learning–based system that automatically predicts the difficulty level (Easy / Medium / Hard) and a numerical difficulty score (1–10) for programming problems using natural language processing (NLP).

## 📌 Project Overview
AutoJudge predicts programing problem difficulty by analyzing problem text and outputs both a categorical difficulty level and a continuous difficulty score. It helps automate difficulty assessment on coding platforms.

## 📂 Dataset Used
- File: problems_data.jsonl
- Format: JSON Lines

Fields:
- title
- description
- input_description
- output_description
- problem_class (Easy / Medium / Hard)
- problem_score (1–10)

## 🧠 Approach & Models Used
- Text preprocessing and cleaning
- TF-IDF (unigrams + bigrams, 15k features)

### Classification Models
- Logistic Regression
- Linear SVM
- Naive Bayes
- KNN
- Random Forest
- XGBoost (best)

### Regression Models
- Ridge (best)
- SVR
- Random Forest
- XGBoost

## 📊 Evaluation Metrics
- Classification: Accuracy,confusion matrix
- Regression: MAE, RMSE

## 🌐 Web Interface
Streamlit-based web app where users enter problem details and get predicted difficulty and score instantly.

## 🚀 Steps to Run the Project Locally

### Step 1: Clone the Repository
Open a terminal or command prompt and run the following command:
```git clone https://github.com/your-username/AutoJudge.git```

### Step 2: Navigate to the Project Directory
Change into the project directory:
```cd AutoJudge```

### Step 3: (Optional) Create and Activate a Virtual Environment
Creating a virtual environment is recommended to avoid dependency conflicts.

Create the virtual environment:
```python -m venv venv```

Activate the virtual environment:

For Windows:
```venv\Scripts\activate```

For Linux / macOS:
```source venv/bin/activate```

### Step 4: Install Required Dependencies
Install all required Python packages using:
```pip install -r requirements.txt```

### Step 5: Run the Streamlit Web Application
Start the Streamlit application using:
```streamlit run app.py```

### Step 6: Access the Application
Once the server starts, open your web browser and go to:
```http://localhost:8501```

The AutoJudge web interface will now be running locally and ready to use.

## 🎥 Demo Video
https://youtu.be/your-demo-video-link

## 👤 Name
**Mayank Lande**  
mayanklande125@gmail.com
9130308422

