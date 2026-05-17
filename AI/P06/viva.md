# Oral Viva Guide - Assignment 6 (Expert System)

## Quick One-Liners

- **Expert System**: Rule-based AI that mimics expert decision making.
- **Knowledge Base**: Stores rules and facts.
- **Inference Engine**: Applies rules to facts to reach conclusions.
- **Library used**: experta.

---

## Core Concept Questions

**Q1. What is an expert system?**
An AI system that uses rules and facts to solve domain problems like a human expert.

**Q2. What are the main components?**
User interface, knowledge base, inference engine.

**Q3. What is the role of the inference engine?**
Matches facts to rules and derives conclusions.

**Q4. What is forward chaining?**
Start from facts and move to conclusions.

---

## Code-Oriented Questions

**Q5. Why use the experta library?**
It provides rule-based logic and inference engine support in Python.

**Q6. What does `@DefFacts` do?**
Defines initial facts that start the reasoning process.

**Q7. What does `@Rule` do?**
Defines a condition-action rule in the knowledge base.

**Q8. What is the purpose of `_ask`?**
Standardizes input and declares symptom facts.

**Q9. How do you add a new symptom?**
Add a new `ask_*` rule and declare a new Fact, then use it in disease rules.

**Q10. How do you add a new disease rule?**
Create a new `@Rule` with a symptom pattern and print a diagnosis.

**Q11. What is `salience=-1` used for?**
Ensures the default rule runs last if no specific disease matches.

**Q12. Why normalize inputs to "yes" or "no"?**
To make rule matching consistent.

---

## Working Flow Questions

**Q13. Explain the execution flow.**
Ask symptoms -> store facts -> match rules -> print diagnosis and treatment.

**Q14. What happens if no rule matches?**
The default rule prints a safe fallback message.

---

## Comparison Questions

**Q15. Expert system vs machine learning?**
Expert systems use fixed rules; ML learns from data.

**Q16. Rule-based AI vs neural networks?**
Rule-based is explainable but limited; neural networks are flexible but less explainable.

---

## External Examiner Questions

**Q17. Can expert systems replace doctors?**
No, they assist but do not replace professionals.

**Q18. What are limitations of expert systems?**
Limited knowledge, no self-learning, and rigid rules.

**Q19. Why is this considered AI?**
It uses symbolic reasoning and rule-based inference.

---

## Common Student Mistakes

- Using outdated `pyknow` instead of experta.
- Missing symptom rules so no facts are created.
- No default rule for unmatched cases.
- Inconsistent input values (not "yes"/"no").

---

## Summary

The system uses experta to declare facts, apply rules, and produce diagnoses. It is a clear example of symbolic, rule-based AI.
