# Supermarket Customer Support Chatbot
# Developed using ChatterBot Library

"""
run this commands:
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install chatterbot
pip install chatterbot_corpus
pip install spacy
python -m spacy download en_core_web_sm
"""

# Import chatbot classes
import re

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot object
bot = ChatBot(
    "SuperMarketBot",
    read_only=True
)

# Create trainer object
trainer = ListTrainer(bot)

# Training data for supermarket customer interaction
conversation = [

    # Greetings
    "hi",
    "Hello! Welcome to Smart Super Market.",

    "hello",
    "Hi! How can I help you today?",

    "hey",
    "Hello! How can I help you today?",

    "good morning",
    "Good morning! How can I help you today?",

    "good evening",
    "Good evening! How can I help you today?",

    # Store timings
    "what are your store timings",
    "Our supermarket is open from 9 AM to 10 PM.",

    "what time do you open",
    "Our supermarket is open from 9 AM to 10 PM.",

    "what time do you close",
    "We close at 10 PM.",

    # Product inquiry
    "do you sell vegetables",
    "Yes, fresh vegetables are available in our supermarket.",

    "do you sell fruits",
    "Yes, we have fresh fruits daily.",

    "do you sell dairy products",
    "Yes, we have milk, cheese, butter, and yogurt.",

    "what products do you have",
    "We have groceries, fresh vegetables, fruits, dairy products, and household items.",

    # Offers and discounts
    "are there any offers today",
    "Yes, there is a 20 percent discount on grocery items.",

    "any discounts",
    "Yes, there is a 20 percent discount on grocery items.",

    # Payment methods
    "what payment methods do you accept",
    "We accept Cash, UPI, Credit Card, Debit Card, and Net Banking.",

    "do you accept upi",
    "Yes, we accept UPI payments.",

    # Delivery
    "do you provide home delivery",
    "Yes, home delivery is available within 5 kilometers.",

    "delivery charges",
    "Delivery is free within 5 kilometers.",

    # Contact information
    "how can i contact customer support",
    "You can contact us at support@smartmarket.com",

    "contact number",
    "You can contact us at support@smartmarket.com",

    # Closing
    "bye",
    "Thank you for visiting Smart Super Market. Have a nice day!",

    "thank you",
    "You're welcome! Happy to help."
]

# Train chatbot with conversation data
trainer.train(conversation)

# Simple normalization and FAQ matching to reduce random replies
def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text)

faq_responses = {
    "hi": "Hello! Welcome to Smart Super Market.",
    "hello": "Hi! How can I help you today?",
    "hey": "Hello! How can I help you today?",
    "good morning": "Good morning! How can I help you today?",
    "good evening": "Good evening! How can I help you today?",
    "what are your store timings": "Our supermarket is open from 9 AM to 10 PM.",
    "what time do you open": "Our supermarket is open from 9 AM to 10 PM.",
    "what time do you close": "We close at 10 PM.",
    "do you sell vegetables": "Yes, fresh vegetables are available in our supermarket.",
    "do you sell fruits": "Yes, we have fresh fruits daily.",
    "do you sell dairy products": "Yes, we have milk, cheese, butter, and yogurt.",
    "what products do you have": "We have groceries, fresh vegetables, fruits, dairy products, and household items.",
    "are there any offers today": "Yes, there is a 20 percent discount on grocery items.",
    "any discounts": "Yes, there is a 20 percent discount on grocery items.",
    "what payment methods do you accept": "We accept Cash, UPI, Credit Card, Debit Card, and Net Banking.",
    "do you accept upi": "Yes, we accept UPI payments.",
    "do you provide home delivery": "Yes, home delivery is available within 5 kilometers.",
    "delivery charges": "Delivery is free within 5 kilometers.",
    "how can i contact customer support": "You can contact us at support@smartmarket.com",
    "contact number": "You can contact us at support@smartmarket.com",
    "bye": "Thank you for visiting Smart Super Market. Have a nice day!",
    "thank you": "You're welcome! Happy to help.",
}

intent_responses = [
    ({"bye", "exit", "quit"}, "Thank you for visiting Smart Super Market. Have a nice day!"),
    ({"thanks", "thank", "thankyou"}, "You're welcome! Happy to help."),
    ({"hi", "hello", "hey", "morning", "evening"}, "Hello! How can I help you today?"),
    ({"timings", "hours", "open", "close", "time"}, "Our supermarket is open from 9 AM to 10 PM."),
    ({"vegetables", "vegetable", "fruits", "fruit", "dairy", "products", "product", "items", "sell"},
     "We have groceries, fresh vegetables, fruits, dairy products, and household items."),
    ({"offer", "offers", "discount", "discounts", "sale"}, "Yes, there is a 20 percent discount on grocery items."),
    ({"payment", "pay", "upi", "card", "cash", "debit", "credit", "netbanking"},
     "We accept Cash, UPI, Credit Card, Debit Card, and Net Banking."),
    ({"delivery", "deliver", "home"}, "Yes, home delivery is available within 5 kilometers."),
    ({"contact", "support", "email", "phone", "number"}, "You can contact us at support@smartmarket.com"),
]

def match_intent(normalized_input: str) -> str | None:
    words = set(normalized_input.split())
    for keywords, response in intent_responses:
        if words & keywords:
            return response
    return None

# Display heading
print("======================================")
print(" SMART SUPERMARKET CHATBOT ")
print("======================================")
print("Type 'bye' to exit.\n")

# Chat loop
while True:

    # Accept user input
    user_input = input("You : ")
    normalized_input = normalize(user_input)

    # Generate chatbot response
    response = faq_responses.get(normalized_input)
    if response is None:
        response = match_intent(normalized_input)
    if response is None:
        response = "Sorry, I didn't understand that. Can you rephrase your question?"

    # Display response
    print("Bot :", response)

    # Exit condition
    if user_input.lower() == "bye":
        break