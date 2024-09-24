import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import google.generativeai as genai
import mysql.connector
from datetime import datetime

#Configure Google API Key
GOOGLE_API_KEY = ' '  #Replace with your Google API Key
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
generation_config = {
    "temperature": 0.65,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model_genai = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Rewrite the following hate speech comment into a positive comment, keeping the sentence structure the same. For example, 'I don't like black people' should be rewritten as 'Black people are great'.",
)

#Initialize chat session
chat_session = model_genai.start_chat()

#Load the classification model and tokenizer
model_path = ''  #Replace with your model path
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="social_media_platform"  
    )
    return conn

def predict_comment(text):
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    return prediction


label_map = {0: "Hate Speech", 1: "Offensive Language", 2: "Neither"}

# Function to classify comment
def classify_comment(text):
    prediction = predict_comment(text)
    return label_map[prediction]

def rephrase_comment(comment):
    try:
        response = chat_session.send_message(comment)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error: {e}")
        return "Rephrasing unsuccessful. Manual review needed."

# Function to log the comment to the database
def log_comment(username, comment, classification, rephrased_comment=None):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO logs (username, comment, classification, timestamp) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (username, comment, classification, datetime.now()))
    conn.commit()
    conn.close()

# Streamlit UI
def user_page():
    st.title("Social Media Platform")

    # Comment section
    comment = st.text_input("Add a comment...", value="", key="comment_input")

    if st.button("Post Comment"):
        if comment:
            classification = classify_comment(comment)
            
            if classification == "Hate Speech":
                rephrased_comment = rephrase_comment(comment)
                st.warning(f"Original comment identified as hate speech. Rephrased comment: {rephrased_comment}")
                log_comment(st.session_state["username"], comment, classification, rephrased_comment)
            
            elif classification == "Offensive Language":
                st.error("Comment flagged as offensive and will not be posted.")
                log_comment(st.session_state["username"], comment, classification)
            
            else:
                st.success("Comment posted successfully!")
                log_comment(st.session_state["username"], comment, classification)
