import streamlit as st
import joblib
import re

# Page Config
st.set_page_config(
    page_title="AutoJudge",
    page_icon="⚖️",
    layout="centered"
)

# Load Models
classifier = joblib.load("final_classifier.pkl")
regressor = joblib.load("final_regressor.pkl")
tfidf = joblib.load("tfidf.pkl")
le = joblib.load("label_encoder.pkl")

# Text Cleaning (MATCH TRAINING)
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Score Adjustment (IMPORTANT)
def adjust_score(score, difficulty):
    difficulty = difficulty.strip().lower()
    score = float(score)
    ranges = {
        "easy": (1.0, 3.5),
        "medium": (3.5, 7.5),
        "hard": (7.5, 10.0)
    }
    low, high = ranges[difficulty]
    return min(max(score, low), high)

# Header
st.title("⚖️ AutoJudge")
st.caption("Predict programming problem difficulty using machine learning")
st.divider()

# Inputs
st.subheader("📝 Problem Details")

title = st.text_input("Title")
description = st.text_area("Problem Description", height=150)
input_desc = st.text_area("Input Description", height=100)
output_desc = st.text_area("Output Description", height=100)

st.divider()

# Predict Button
if st.button("🚀 Predict Difficulty"):
    if not title or not description:
        st.warning("Please enter at least **Title** and **Problem Description**.")
    else:
        text = clean_text(
            title + " " + description + " " + input_desc + " " + output_desc
        )
        vec = tfidf.transform([text])

        class_idx = classifier.predict(vec)[0]
        pred_class = le.inverse_transform([class_idx])[0]

        raw_score = float(regressor.predict(vec)[0])
        final_score = adjust_score(raw_score, pred_class)

        # Results
        st.success(f"🎯 Difficulty Level: **{pred_class.upper()}**")

        st.metric(
            label="📊 Difficulty Score",
            value=f"{final_score:.2f} / 10"
        )

        st.progress(final_score / 10)

# Footer
st.divider()
st.caption("AutoJudge Project | ML-based Classification & Regression")
