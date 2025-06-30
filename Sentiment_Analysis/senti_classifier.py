import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import os

# Load your trained model
model_path = "./my_senti_model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Create pipeline
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Excel file path
excel_file = "sentiment_results.xlsx"

# UI
st.title("Shreevikas,s Movie Review Sentiment Analyzer")
st.write("Enter a movie name and your review. I'll tell you if it's Positive or Negative — and save it too!")

movie_name = st.text_input("Enter Movie Name ", "")
user_review = st.text_area("Type your review here ", "")

# Check if review looks legit
def looks_like_review(text):
    keywords = ["movie", "film", "story", "acting", "funny", "boring", "interesting", "awesome",
        "bad", "good", "amazing", "terrible", "memorable", "forgettable", "slow", "fast",
        "love", "hate", "liked", "disliked", "enjoyed", "performance", "plot", "scene"]
    text = text.lower()
    return any(word in text for word in keywords)

if st.button("Analyze and Save"):
    if movie_name.strip() == "" or user_review.strip() == "":
        st.warning("Please fill in both the movie name and review.")
    elif not looks_like_review(user_review):
        st.info("🤖 That doesn't look like a review. Please describe how you felt about the movie.")
    else:
        # Run sentiment analysis
        result = classifier(user_review)[0]
        label_map = {
            "LABEL_0": "Negative 😞",
            "LABEL_1": "Positive 😊"
        }
        sentiment = label_map.get(result["label"], result["label"])
        confidence = result["score"]

        # Show result
        st.success(f"**Prediction:** {sentiment}")
        st.markdown(f"**Confidence:** `{confidence:.2f}`")

        # Save to Excel
        new_data = pd.DataFrame([{
            "Movie Name": movie_name,
            "Review": user_review,
            "Sentiment": sentiment,
            "Confidence": round(confidence, 2)
        }])

        # If file exists, append. Else, create.
        if os.path.exists(excel_file):
            existing_data = pd.read_excel(excel_file)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            updated_data = new_data

        updated_data.to_excel(excel_file, index=False)
        st.success(" Review and sentiment saved to Excel! Thank-you")
