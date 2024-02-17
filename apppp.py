import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'model.pkl' exists in the specified location.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")
    st.stop()

# Load the vectorizer used during training
try:
    with open('cv.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError:
    st.error("Vectorizer file not found. Make sure 'vectorizer.pkl' exists in the specified location.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the vectorizer: {str(e)}")
    st.stop()

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    user_input = [q1, q2]

    try:
        # Transform the user input using the loaded vectorizer
        user_input_transformed = vectorizer.transform(user_input).toarray()

        result = model.predict(user_input_transformed)

        if result:
            st.header('Duplicate')
        else:
            st.header('Not Duplicate')
    except Exception as e:
        st.error(f"Error predicting: {str(e)}")
