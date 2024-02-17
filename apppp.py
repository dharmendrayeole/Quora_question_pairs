import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    user_input = np.array([q1,q2])
    result = model.predict(user_input)

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')