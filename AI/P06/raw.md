## Assignment No. 6

### Title

Implementation of Expert System for Hospital and Medical Facilities

### Aim

To implement an expert system for hospital and medical facilities using Python.

### Objectives

- Understand expert systems in AI.
- Implement a medical diagnosis expert system.
- Simulate hospital and medical consultation.
- Use rule-based reasoning for disease prediction.
- Understand inference engine and knowledge base concepts.

### Problem Statement

Implement an expert system for hospital and medical facilities.

### Software Requirements

| Requirement | Details |
| --- | --- |
| Operating System | Windows 7/8/10/11 |
| Programming Language | Python |
| IDE | VS Code / PyCharm |
| Library | experta (pyknow alternative) |

### Hardware Requirements

| Requirement | Details |
| --- | --- |
| Processor | Intel Core i3/i5 or above |
| RAM | 4GB minimum |
| Device | PC / Laptop |

## Theory

### What is an Expert System?

#### Beginner Explanation

An expert system is a computer program that behaves like a human expert. It asks questions, analyzes answers, and gives decisions or suggestions.

Examples:

- Medical diagnosis systems
- Banking advisory systems
- Troubleshooting systems

#### Technical Definition

An expert system is an AI-based decision-making system that uses knowledge, facts, logical reasoning, and predefined rules to solve domain-specific problems.

### Components of Expert System

1. **User Interface**: Allows interaction between user and system.
2. **Knowledge Base**: Stores facts, rules, and domain knowledge.
3. **Inference Engine**: Applies rules to facts and derives conclusions.

### Expert System Architecture

```text
User
-> Input Symptoms
-> Inference Engine
-> Knowledge Base
-> Rule Matching
-> Disease Prediction
-> Display Treatment
```

### Knowledge Base

Stores medical knowledge such as symptom-to-disease rules.

### Inference Engine

Compares rules, identifies matches, and produces results.

### Chaining Methods

- **Forward Chaining**: Starts from facts and moves to conclusion.
- **Backward Chaining**: Starts from a goal and checks supporting facts.

### Why This Practical Uses Rule-Based AI

- Diseases are predicted using predefined rules.
- Symptoms are matched logically.
- No deep learning required.

## Important Note About Practical

The journal code is large and outdated. This practical uses the **experta** library instead of **pyknow**.

### Installation Command

```bash
pip install experta
```

## Project Structure

```text
Medical_Expert_System
│
├── expertsystem.py
├── requirements.txt
└── output.txt
```

## Proper Practical-Friendly Python Code

```python
# Expert System for Hospital and Medical Facilities

from experta import *

# Define expert system
class MedicalExpertSystem(KnowledgeEngine):

    # Initial message
    @DefFacts()
    def initial_facts(self):

        print("===================================")
        print(" MEDICAL EXPERT SYSTEM ")
        print("===================================")

        print("\nAnswer the following questions with yes/no:\n")

        yield Fact(action="diagnose")

    # Pattern for adding new symptoms:
    # 1) Add an ask_* rule that declares a Fact for the symptom.
    # 2) Use that Fact in one or more disease rules below.
    # 3) Add an outcome message in the matched rule.
    def _ask(self, prompt, fact_name):
        answer = input(prompt).strip().lower()
        if answer not in {"yes", "no"}:
            answer = "no"
        self.declare(Fact(**{fact_name: answer}))

    # Ask symptoms
    @Rule(Fact(action="diagnose"), NOT(Fact(fever=W())))
    def ask_fever(self):
        self._ask("Do you have fever? ", "fever")

    @Rule(Fact(action="diagnose"), NOT(Fact(cough=W())))
    def ask_cough(self):
        self._ask("Do you have cough? ", "cough")

    @Rule(Fact(action="diagnose"), NOT(Fact(headache=W())))
    def ask_headache(self):
        self._ask("Do you have headache? ", "headache")

    @Rule(Fact(action="diagnose"), NOT(Fact(sore_throat=W())))
    def ask_sore_throat(self):
        self._ask("Do you have sore throat? ", "sore_throat")

    @Rule(Fact(action="diagnose"), NOT(Fact(fatigue=W())))
    def ask_fatigue(self):
        self._ask("Do you feel fatigue? ", "fatigue")

    @Rule(Fact(action="diagnose"), NOT(Fact(body_ache=W())))
    def ask_body_ache(self):
        self._ask("Do you have body ache? ", "body_ache")

    # Disease rules
    @Rule(
        Fact(fever="yes"),
        Fact(cough="yes"),
        Fact(headache="yes"),
        Fact(body_ache="yes"),
    )
    def flu(self):
        print("\nPossible Disease : Flu")
        print("Treatment : Take rest, drink fluids, and consult doctor.")

    @Rule(
        Fact(fever="no"),
        Fact(cough="yes"),
        Fact(sore_throat="yes"),
        Fact(headache="no"),
    )
    def cold(self):
        print("\nPossible Disease : Common Cold")
        print("Treatment : Steam inhalation and proper rest.")

    @Rule(Fact(fever="no"), Fact(cough="no"), Fact(headache="yes"))
    def migraine(self):
        print("\nPossible Disease : Migraine")
        print("Treatment : Reduce stress and consult neurologist.")

    @Rule(
        Fact(fever="no"),
        Fact(cough="yes"),
        Fact(sore_throat="yes"),
        Fact(fatigue="yes"),
    )
    def viral_pharyngitis(self):
        print("\nPossible Disease : Viral Pharyngitis")
        print("Treatment : Warm fluids, rest, and consult doctor if severe.")

    @Rule(
        Fact(fever="no"),
        Fact(cough="no"),
        Fact(sore_throat="yes"),
        Fact(headache="no"),
    )
    def throat_irritation(self):
        print("\nPossible Condition : Throat Irritation")
        print("Treatment : Hydration and avoid irritants.")

    # Default rule
    @Rule(
        Fact(fever=MATCH.f1),
        Fact(cough=MATCH.f2),
        Fact(headache=MATCH.f3),
        Fact(sore_throat=MATCH.f4),
        Fact(fatigue=MATCH.f5),
        Fact(body_ache=MATCH.f6),
        salience=-1,
    )
    def no_disease(self, f1, f2, f3, f4, f5, f6):
        print("\nDisease not identified exactly.")
        print("Please consult a medical professional.")


# Driver Code
engine = MedicalExpertSystem()
engine.reset()
engine.run()
```

## Why This Code Is Better for Practical

- Runs properly in modern Python using experta.
- Implements expert system architecture (facts, rules, inference engine).
- Simple, clear, and easy to explain in viva.
- Matches the hospital application requirement.

## Where Knowledge Base Exists

Example rule block:

```python
@Rule(Fact(fever="yes"), Fact(cough="yes"), Fact(headache="yes"))
```

This stores medical knowledge for a specific disease pattern.

## Where Inference Engine Works

The experta engine evaluates facts, applies rules, and derives conclusions.

## Execution Flow

```text
User Inputs Symptoms
-> Facts Stored
-> Inference Engine Activated
-> Rules Matched
-> Disease Predicted
-> Treatment Displayed
```

## Expected Output (Example)

```text
===================================
 MEDICAL EXPERT SYSTEM
===================================

Answer the following questions with yes/no:

Do you have fever? yes
Do you have cough? yes
Do you have headache? yes
Do you have sore throat? no
Do you feel fatigue? yes
Do you have body ache? yes

Possible Disease : Flu
Treatment : Take rest, drink fluids, and consult doctor.
```

## Difference Table

### Expert System vs Normal Program

| Feature | Expert System | Normal Program |
| --- | --- | --- |
| Decision Making | Intelligent | Fixed |
| Knowledge Base | Yes | No |
| Reasoning | Yes | Limited |
| Rule Processing | Yes | Minimal |

### Rule-Based AI vs Machine Learning

| Feature | Rule-Based | ML-Based |
| --- | --- | --- |
| Learning | No | Yes |
| Rules | Predefined | Learned |
| Complexity | Lower | Higher |
| Explainability | High | Lower |

## Common Viva Questions

### Basic Viva

**What is an expert system?**
AI system that mimics human expert decision making.

**What is knowledge base?**
Collection of facts and rules.

**What is inference engine?**
Decision-making component of an expert system.

**Which AI approach used here?**
Rule-based AI.

**Why experta library used?**
To implement expert system rules easily.

### Advanced Viva

**Difference between forward and backward chaining?**
Forward uses facts to conclusion; backward uses goal to facts.

**Is this machine learning?**
No, this is rule-based expert system.

**Can expert systems replace doctors?**
No, they assist doctors but cannot fully replace them.

**What are limitations of expert systems?**
Limited knowledge and no self-learning.

### External Examiner Trap Questions

| Question | Smart Answer |
| --- | --- |
| Is this true AI? | Yes, rule-based symbolic AI |
| Does it learn automatically? | No |
| Why not deep learning? | Practical focuses on expert systems |
| What if no rule matches? | Default rule handles unmatched cases |

## Common Student Mistakes

| Mistake | Problem |
| --- | --- |
| Using outdated pyknow | Import errors |
| Missing rules | No diagnosis |
| Incorrect fact matching | Wrong output |
| No default condition | Program fails to answer |

## Most Important One-Liners

| Question | Quick Answer |
| --- | --- |
| AI Technique | Expert System |
| Domain | Medical Diagnosis |
| Library Used | experta |
| Reasoning Type | Rule-Based |
| Core Component | Inference Engine |

## Conclusion

Successfully implemented an expert system for hospital and medical facilities using rule-based reasoning and an inference engine in Python.
