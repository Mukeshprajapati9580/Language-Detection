import streamlit as st
import pickle

# -----------------------------
# Load trained model & vectorizer
# -----------------------------
with open("language_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("count_vectorizer.pkl", "rb") as file:
    cv = pickle.load(file)


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Language Detection",
    page_icon="🌐",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🌐 Language Detection")
st.write("Enter a sentence and the model will predict its language.")


# -----------------------------
# Text Input
# -----------------------------
user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: Bonjour, comment allez-vous ?",
    height=150
)


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Detect Language"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")

    else:
        # Convert text using the same CountVectorizer
        data = cv.transform([user_text]).toarray()

        # Predict language
        output = model.predict(data)

        # Display result
        st.success(f"Detected Language: {output[0]}")
