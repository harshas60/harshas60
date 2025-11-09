import random, re

patterns = {
    r"(hi|hello|hey)": [
        "Hello there!",
        "Hi!",
        "Hey!",
        "Greetings!",
        "Nice to meet you!"
    ],
    r"(how are you|how's it going)": [
        "I'm doing well, thank you.",
        "I'm great, how about you?",
        "All systems are running smoothly!",
        "Feeling chatty, as always!"
    ],
    r"(what's your name|who are you)": [
        "I'm a simple chatbot.",
        "I'm a friendly chatbot.",
        "I'm your virtual assistant.",
        "Just call me Chatbot!"
    ],
    r"(what do you do|what's your purpose)": [
        "I chat with awesome people like you!",
        "I answer questions and keep you company.",
        "I'm here to assist and entertain!",
        "Helping and chatting is my purpose."
    ],
    r"(bye|goodbye)": [
        "Goodbye!",
        "See you later!",
        "Take care!",
        "Catch you next time!"
    ],
    r"(what's the weather|is it sunny)": [
        "I'm not great with weather forecasts, but I hope it's sunny!",
        "Weather predictions aren't my specialty, but it feels warm in here!",
        "I can't check the weather, but you can try asking a weather app."
    ],
    r"(tell me a joke|make me laugh)": [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don’t scientists trust atoms? Because they make up everything.",
        "Why did the math book look sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!",
        "Why couldn’t the bicycle stand up by itself? It was two tired.",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "Why don’t eggs tell jokes? They’d crack each other up!",
        "What do you call cheese that isn’t yours? Nacho cheese.",
        "Why did the tomato turn red? Because it saw the salad dressing!"
    ],
    r"(i'm (.*)|i am (.*))": [
        "Nice to meet you, {1}!",
        "Hello, {1}! How can I help you today?",
        "It's great to chat with you, {1}!"
    ],
    r"(.*)": [
        "I'm not sure how to respond to that.",
        "Could you rephrase that?",
        "Interesting! Tell me more.",
        "Let's chat about something else. What’s on your mind?"
    ]  # Default response
}
def chatbot_response(user_input):
    for pattern, responses in patterns.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if "{1}" in response:
                response = response.format(*match.groups())
            return response
    return "I'm not sure how to respond to that."  # Fallback default response

print("Welcome to the chatbot! Type 'bye' to exit.")
while True:
    query = input("You: ")
    if query.lower() == 'bye' or query.lower()=="goodbye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(query)
    print("Chatbot:", response)