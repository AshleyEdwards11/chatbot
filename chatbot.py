import re

# Define some predefined responses
responses = {
    "hi": "Hello!",
    "bye": "Goodbye!",
    "how are you": "I'm doing well, thank you!",
    "default": "I'm sorry, I didn't understand what you said."
}

def respond(message):
    # check for a match in the predefined responses
    for pattern, response in responses.items():
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return response
    # if no match is found, return the default response
    return responses["default"]

while True:
    message = input("You: ")
    if message.lower() in ["bye", "goodbye"]:
        print(respond(message))
        break
    print("Chatbot: " + respond(message))
