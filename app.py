import streamlit as st
import json
import random
import joblib

model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

with open("intents.json", "r") as file:
    intents = json.load(file)

st.title("Customer Service Chatbot")

user_input = st.text_input("Ask a question")

if st.button("Send"):

    X = vectorizer.transform([user_input])

    prediction = model.predict(X)[0]

    response = "Sorry, I don't understand."

    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            response = random.choice(intent["responses"])

    st.success(response)