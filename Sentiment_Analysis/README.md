# 🎭 Sentiment Analysis of Movie Reviews using BERT

This is a simple **Sentiment Analysis** project that classifies user movie reviews into **Positive**, **Negative**, or **Neutral** sentiments using **BERT** and a minimal **Streamlit** interface.

> ⚠️ *This is a work-in-progress project and may not perform well on sarcastic or highly nuanced reviews. An upgraded model with sarcasm detection is under development.*

---

## 🚀 Features

- Classifies free-text movie reviews into **Positive**, **Negative**, or **Neutral**
- Simple and interactive **Streamlit** UI
- Stores each review, its sentiment, and the movie name in an Excel file
- Built using a fine-tuned **BERT-based classifier**
- Modular code for easy updates and improvements

---

## 🧠 Technologies Used

- **BERT (bert-base-uncased)** — via 🤗 Hugging Face Transformers
- **PyTorch** — for model fine-tuning
- **Streamlit** — to create a simple web interface
- **Pandas** — for saving data to Excel
- **IMDb Dataset** — for training


---

## ⚠️ Known Limitations

- Sarcastic reviews like _"Best movie ever, I only fell asleep twice."_ are **not yet accurately classified**.
- Working on adding sarcasm detection using a custom sarcasm classification model in the next version.

---

## 👨‍💻 Author

**Shreevikas B J**  
---

## 📌 To-Do

- [x] Train BERT model on IMDb dataset
- [x] Create Streamlit interface
- [x] Save reviews to Excel
- [ ] Integrate sarcasm detection model
- [ ] Improve accuracy on ambiguous inputs

---

## ⭐️ Give a Star

If you found this helpful, feel free to ⭐ the repo and share your feedback!
