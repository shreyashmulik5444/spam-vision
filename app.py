# 🔹 1. Imports (TOP of file)
import streamlit as st
import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer



nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)


# 🔹 3. Initialize objects
ps = PorterStemmer()


# 🔹 4. Preprocessing function
def text_transform(text):
    
    text = text.lower()
    words = word_tokenize(text)
    stop_words = stopwords.words('english')
    
    cleaned_words = []
    
    for word in words:
        if word.isalpha() and word not in stop_words:
            cleaned_words.append(ps.stem(word))
    
    return " ".join(cleaned_words)


# 🔹 5. Load model + vectorizer
cv = pickle.load(open('Vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))


# 🔹 6. Streamlit UI
st.title("Email/SMS Spam Detection Engine")

input_text = st.text_area(
    "Enter your message here",  # <-- label (required)
    placeholder="Enter the Message to check spam"
)


# 🔹 7. Prediction (ONLY when button clicked)
if st.button("Predict"):
    
    # preprocess
    transformed_sms = text_transform(input_text)
    
    # vectorize
    vector_input = cv.transform([transformed_sms])
    
    # predict
    result = model.predict(vector_input)[0]
    
    # display
    if result == 1:
        st.header('Spam 🚨')
    else:
        st.header(' Not Spam')