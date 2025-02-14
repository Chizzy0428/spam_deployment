import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit App
st.title("Spam Message Classifier")
st.write("Enter a message below to check if it's spam or not.")

# Input from user
message = st.text_area("Enter message:")

if st.button("Check Message"):
    if message:
        prediction = model.predict([message])
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a message to classify.")
