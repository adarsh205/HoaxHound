import streamlit as st
import joblib
model = joblib.load('hoaxhoundmodel')
st.title('Hoax Hound - Fake News Detection')
ip = st.text_input('enter the text')
op = model.predict([ip])
if st.button('Predict'):  #a button will be created named 'Predict'
  st.title(op[0])    #output will be displayed as a title
