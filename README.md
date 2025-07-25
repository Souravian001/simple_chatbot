# 🤖 Simple AI Chatbot

This is a basic AI chatbot built using Python, Scikit-learn, and natural language processing techniques. The bot uses intent classification to provide responses to user queries based on predefined patterns.

---

## 🧠 Features

- Intent classification using `LogisticRegression`
- Text preprocessing using `TfidfVectorizer`
- JSON-based training data
- Simple command-line interface for chatting

---

## 🗂️ Project Structure

```
simple_chatbot/
│
├── intents.json       # Contains intents, patterns, and responses
├── train.py           # Trains the intent classification model
├── chat.py            # Chat interface for interacting with the bot
└── model.pkl          # Saved trained model (auto-generated)
```

---

## 📦 Requirements

- Python 3.x
- scikit-learn
- numpy
- pickle

Install dependencies:

```bash
pip install scikit-learn numpy
```

---

## 🚀 How to Run

1. **Train the model**

```bash
python train.py
```

This will train the model and save `model.pkl` and `vectorizer.pkl`.

2. **Chat with the bot**

```bash
python chat.py
```
---

## 🧾 Example `intents.json`

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you", "Goodbye"],
      "responses": ["Bye!", "Take care!", "See you soon!"]
    }
  ]
}
```

---

## 📌 Notes
- it can be expanded by adding more tags, patterns, and responses to `intents.json`.
- The model can be improved further with NLP libraries like spaCy or NLTK, or even deep learning with PyTorch or TensorFlow.

---
## 📄 License

This project is open source and available under the [MIT License](LICENSE).
