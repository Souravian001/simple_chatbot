import json
import pickle
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open('intents.json') as file:
    data = json.load(file)

corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
pickle.dump(model, open('chatbot_model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("✅ Model trained and saved!")
