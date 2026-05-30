# Rule Based AI python ChatBot

import datetime
import time

name = input("Swagat h, Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon", name)
elif 17 <= presentHour <= 20:
    print("Good Evening", name)
else:
    print("Good Night", name)

print("Namaste! Welcome to Your ChatBot 🤖")
print("You can ask me basic questions. Type 'bye' to exit.\n")

# Chatbot memory (dictionary of responses)

responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "how are you": "I am fine. Thank you for asking!",
    "who are you": "I am a Smart AI ChatBot.",
    "motivate me": "Keep going! Every bug in your project makes you a better developer.",
    "happy": "Great to hear that! 😊",
    "function kya hote hai": "Functions reusable blocks of code hote hain jo code ko organize aur reuse karne me help karte hain."
}

# Function to get chatbot response

def get_response_of_bot(user_question):
    user_question = user_question.lower()

    for key in responses:
        if key in user_question:
            return responses[key]

    return "Sorry, mujhe abhi iska answer nahi pata. Main abhi learning mode me hoon."

# Main chatbot loop

while True:

    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    reply = get_response_of_bot(user_input)

    print("Bot:", reply)

