# 🚀 SpamVision – Email/SMS Spam Detection Engine

## 📌 Overview
SpamVision is a Machine Learning-based web application that detects whether a given message is Spam or Ham (Not Spam) using Natural Language Processing (NLP).

The model is trained on email/SMS data and deployed using Streamlit Cloud for real-time predictions.

---

## 🌐 Live Demo
👉 https://shreyashmulik5444-spamvision-app-btku1p.streamlit.app/

---

## 🧠 Problem Statement
Spam messages are a common issue in communication systems. This project aims to build an intelligent system that can automatically classify messages as:

- Spam (Unwanted messages)
- Ham (Legitimate messages)

---

## ⚙️ Tech Stack
- Python
- Pandas & NumPy
- NLTK (Natural Language Processing)
- Scikit-learn
- Streamlit (for deployment)

---

## 🔍 Machine Learning Approach

### 1. Data Preprocessing
- Removed duplicates
- Handled null values
- Tokenization using NLTK
- Removed stopwords
- Stemming using Porter Stemmer
- Converted text to lowercase

---

### 2. Feature Engineering
- Text converted into numerical form using:
  - CountVectorizer

---

### 3. Model Used
- Naive Bayes Classifier
  - Efficient for text classification
  - Works well with high-dimensional data

---

### 4. Exploratory Data Analysis (EDA)
- Analyzed:
  - Character count
  - Word count
  - Sentence count
- Compared distributions between spam and ham
- Used:
  - Histograms
  - Pairplots
  - Correlation heatmap

---

## 📊 Key Insights
- Spam messages generally have:
  - More characters
  - More words
  - Different distribution patterns compared to ham
- Dataset was imbalanced (ham > spam)

---

## 🚀 Features
- Real-time spam detection
- Simple and clean UI
- Fast predictions
- Handles custom user input

---

## 🖥️ How to Run Locally


# Clone repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/shreyashmulik5444/spam-vision)

# Navigate to project folder
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py


## 📂 Dataset
Dataset used for training:
👉 [https://www.kaggle.com/datasets/your-dataset-link](https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset)
