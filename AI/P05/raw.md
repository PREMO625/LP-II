## Assignment No. 5

### Title

Development of an Elementary Chatbot for Customer Interaction Application

### Aim

To develop an elementary chatbot for customer interaction application using Python.

### Objectives

- Understand chatbot systems.
- Implement a rule-based chatbot.
- Simulate customer interaction using AI.
- Understand NLP basics.
- Generate automated responses to user queries.

### Problem Statement

Develop an elementary chatbot for any suitable customer interaction application.

### Software Requirements

| Requirement | Details |
| --- | --- |
| Operating System | Windows 7/8/10/11 |
| Programming Language | Python |
| IDE | VS Code / PyCharm |
| Library | ChatterBot |

### Hardware Requirements

| Requirement | Details |
| --- | --- |
| Processor | Intel Core i3/i5 or above |
| RAM | 4GB minimum |
| Device | PC / Laptop |

## Theory

### What is a Chatbot?

#### Beginner Explanation

A chatbot is a software application that can communicate with humans using text or voice. It behaves like a virtual assistant.

Examples:

- Siri
- Alexa
- ChatGPT
- Customer support bots

#### Technical Definition

A chatbot is an AI-based software designed to simulate human conversation using NLP, machine learning, and predefined rules.

### Why Chatbots Are Important

Chatbots help businesses:

- Automate customer support.
- Reduce human workload.
- Provide instant responses.
- Improve customer experience.

### Real World Applications

| Application | Usage |
| --- | --- |
| Banking | Customer support |
| E-Commerce | Order tracking |
| Healthcare | Appointment systems |
| Education | Student assistance |
| Websites | FAQ support |

### Types of Chatbots

#### 1. Rule-Based Chatbots

These chatbots follow predefined rules and answer fixed questions.

Advantages:

- Simple
- Fast
- Easy to implement

Disadvantages:

- Cannot handle complex queries
- Limited intelligence

#### 2. Self-Learning Chatbots

These use AI, ML, and NLP. They improve over time.

| Type | Description |
| --- | --- |
| Retrieval-Based | Select predefined best response |
| Generative | Generate completely new responses |

This practical uses a **retrieval-based** chatbot approach.

### Natural Language Processing (NLP)

NLP allows computers to understand human language: text processing, meaning identification, and response generation.

### ChatterBot Library

ChatterBot is a Python library used to create conversational chatbots. It learns from conversations, stores responses, and generates replies.

#### How ChatterBot Works

```text
User Input
-> Pattern Matching
-> Find Closest Statement
-> Select Best Response
-> Display Reply
```

### Chatbot Workflow

```text
User Query
-> Text Processing
-> Search Matching Pattern
-> Select Best Response
-> Return Output
```

## Important Note About Practical

The journal code contains syntax errors and formatting mistakes. The code below is clean, runnable, and viva friendly.

## Project Structure

```text
Chatbot_Project
│
├── chatbot.py
├── requirements.txt
└── output.txt
```

### Installation Commands

```bash
pip install chatterbot
pip install chatterbot_corpus
```

## Correct and Simple Python Code

```python
# Import chatbot classes
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot(
    "PyBot",
    read_only=True
)

# Create trainer object
trainer = ListTrainer(bot)

# Training data
conversation = [
    "Hi",
    "Hello",
    "How are you?",
    "I am fine.",
    "What is your name?",
    "My name is PyBot.",
    "What is AI?",
    "AI stands for Artificial Intelligence.",
    "Bye",
    "Goodbye"
]

# Train chatbot
trainer.train(conversation)

# Chat loop
while True:

    user_input = input("You : ")

    # Exit condition
    if user_input.lower() == "bye":
        print("Bot : Goodbye")
        break

    # Generate response
    response = bot.get_response(user_input)

    print("Bot :", response)
```

## Line-by-Line Explanation

### Import Libraries

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
```

Imports the chatbot class and a list-based trainer.

### Create Chatbot

`ChatBot("PyBot")` creates the chatbot object.

### Training Data

`conversation` stores question-answer pairs.

### Training Step

`trainer.train(conversation)` teaches the chatbot the patterns.

### Chat Loop

`bot.get_response(user_input)` produces a reply.

## Execution Flow

```text
User Input
-> Chatbot Receives Query
-> Pattern Matching
-> Find Closest Response
-> Generate Reply
-> Display Output
```

## Expected Output

```text
You : Hi
Bot : Hello

You : How are you?
Bot : I am fine.

You : What is AI?
Bot : AI stands for Artificial Intelligence.

You : Bye
Bot : Goodbye
```

## Why This is AI-Based

Even though simple, the chatbot demonstrates NLP and conversational AI using pattern matching.

## Time Complexity

| Operation | Complexity |
| --- | --- |
| Response Matching | $O(N)$ |

## Space Complexity

| Complexity |
| --- |
| $O(N)$ |

## Difference Table

### Rule-Based vs AI Chatbots

| Feature | Rule-Based | AI-Based |
| --- | --- | --- |
| Intelligence | Low | High |
| Learning | No | Yes |
| Flexibility | Limited | Dynamic |
| Complexity | Simple | Complex |

### Retrieval vs Generative Chatbots

| Feature | Retrieval | Generative |
| --- | --- | --- |
| Response Type | Predefined | Generated |
| Complexity | Lower | Higher |
| Speed | Faster | Slower |
| Example | FAQ Bots | ChatGPT |

## Common Viva Questions

### Basic Viva

**What is a chatbot?**
Software that communicates with humans using text or voice.

**What is NLP?**
Natural Language Processing.

**Which type of chatbot is implemented here?**
Retrieval-based chatbot.

**What is ChatterBot?**
Python library for chatbot development.

**Why training is required?**
To teach chatbot responses.

### Advanced Viva

**Difference between retrieval and generative chatbot?**
Retrieval selects predefined response; generative creates new responses.

**Why chatbot is an AI application?**
Because it simulates human interaction using NLP.

**Can this chatbot learn automatically?**
Basic version learns only from training data.

**What are limitations of rule-based chatbot?**
Cannot handle complex or unknown queries.

### External Examiner Trap Questions

| Question | Smart Answer |
| --- | --- |
| Is this true AI? | Basic conversational AI |
| Does it use Machine Learning? | ChatterBot uses ML-style matching |
| Why not use ChatGPT API? | This practical focuses on an elementary chatbot |
| Can it handle voice? | Not in the current implementation |

## Common Student Mistakes

| Mistake | Problem |
| --- | --- |
| Wrong library installation | Import error |
| Incorrect training format | Bot gives wrong replies |
| Infinite loop issue | Program never exits |
| No exit condition | User cannot terminate chatbot |

## Most Important One-Liners

| Question | Quick Answer |
| --- | --- |
| Chatbot Type | Retrieval-Based |
| Library Used | ChatterBot |
| AI Field | NLP |
| Main Purpose | Customer interaction |
| Training Method | List training |

## Conclusion

Successfully developed an elementary chatbot for customer interaction using Python and ChatterBot.
