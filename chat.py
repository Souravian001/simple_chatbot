# Load model & vectorizer
model = pickle.load(open('chatbot_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

print("🤖 ChatBot is ready! (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        break

    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]

    for intent in data['intents']:
        if intent['tag'] == prediction:
            print("Bot:", random.choice(intent['responses']))
