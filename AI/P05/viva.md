# Oral Viva Guide - Assignment 5 (Chatbot)

## Quick One-Liners

- **Chatbot**: Program that interacts using text or voice.
- **Type used**: Retrieval-based chatbot.
- **Library**: ChatterBot with ListTrainer.
- **Core idea**: Match input to closest known statement.

---

## Core Concept Questions

**Q1. What is a chatbot?**
A software system that simulates human conversation.

**Q2. What is NLP?**
Natural Language Processing, which helps computers understand text.

**Q3. What type of chatbot is implemented here?**
Retrieval-based chatbot.

---

## Code-Oriented Questions

**Q4. Why use ChatterBot?**
It provides ready-to-use chatbot classes and training utilities.

**Q5. What is `ListTrainer`?**
A trainer that learns from a list of question-answer pairs.

**Q6. Why set `read_only=True`?**
Prevents the bot from learning new responses during chat.

**Q7. How does `get_response` work?**
It finds the closest match in the training data and returns a response.

**Q8. Why add an exit condition?**
To stop the infinite loop cleanly when the user types "bye".

---

## Working Flow Questions

**Q9. Explain the execution flow.**
Input -> match to known patterns -> return best response -> print output.

**Q10. Why is training required?**
The bot needs example conversations to match user inputs.

---

## Complexity Questions

**Q11. What is the response matching complexity?**
Roughly $O(N)$, where $N$ is the number of training statements.

---

## Comparison Questions

**Q12. Retrieval vs Generative chatbot?**
Retrieval selects predefined responses; generative creates new responses.

**Q13. Rule-based vs AI-based chatbot?**
Rule-based follows fixed rules; AI-based can learn and generalize.

---

## External Examiner Questions

**Q14. Is this real AI?**
Yes, a basic conversational AI using NLP and pattern matching.

**Q15. Does it use machine learning?**
ChatterBot uses ML-style matching, but the system is still simple.

**Q16. Can it handle voice?**
Not in this implementation.

---

## Common Student Mistakes

- Not installing ChatterBot correctly.
- Wrong conversation format for training.
- Missing exit condition.
- Expecting the bot to answer unknown questions perfectly.

---

## Summary

The chatbot is retrieval-based, trained with sample conversations, and uses ChatterBot's matching engine to respond to user inputs.
