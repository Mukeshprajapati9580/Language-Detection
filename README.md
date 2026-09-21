# 🌐 Language Detection

A machine learning project that detects the language of a given text.

## 📌 Project Overview

This project uses Natural Language Processing and Machine Learning to identify the language of input text.


## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* CountVectorizer
* Multinomial Naive Bayes
* Streamlit
* Jupyter Notebook

## 📂 Project Structure

Language-Detection/
│
├── README.md
├── app.py
├── Code.ipynb
├── language_model.pkl
├── count_vectorizer.pkl
├── requirements.txt
└── .gitignore

## ⚙️ Installation

Clone the repository:

git clone https://github.com/Mukeshprajapati9580/Language-Detection


Install the required libraries:

pip install -r requirements.txt

## ▶️ Run the Streamlit Application

Run:

streamlit run app.py

The application will open in your browser.

## 🔍 How It Works

1. User enters a sentence or paragraph.
2. The text is transformed using the trained CountVectorizer.
3. The trained machine learning model processes the transformed text.
4. The predicted language is displayed in the Streamlit interface.
