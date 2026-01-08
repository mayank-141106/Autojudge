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
- Ridge
- SVR
- Random Forest
- XGBoost (best)

## 📊 Evaluation Metrics
- Classification: Accuracy,confusion matrix
- Regression: MAE, RMSE

## 🌐 Web Interface
Streamlit-based web app where users enter problem details and get predicted difficulty and score instantly.

## 🚀 Steps to Run Locally
```bash
git clone https://github.com/your-username/AutoJudge.git
cd AutoJudge
pip install -r requirements.txt
streamlit run app.py
```

## 🎥 Demo Video
https://youtu.be/your-demo-video-link

## 👤 Name
**Mayank Lande**  

