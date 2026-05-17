# Oral Viva Guide - CC P03 (Salesforce Apex)

## Quick One-Liners

- **Apex**: Salesforce proprietary, strongly typed, Java-like language.
- **Apex Class**: Similar to a Java class; contains methods and logic.
- **System.debug**: Prints output to debug logs.
- **Execute Anonymous**: Runs code without saving as a class.

---

## Basic Questions

1. What is Salesforce?
   - A cloud CRM platform.
2. What is Apex?
   - Salesforce programming language for business logic.
3. Where is Apex code executed?
   - On the Salesforce cloud (Force.com platform).
4. What is an Apex class?
   - A container for methods and logic.
5. What is Developer Console?
   - Browser-based IDE for Apex code.
6. What is System.debug?
   - Sends output to the debug log.
7. What is Execute Anonymous window?
   - Runs Apex code on demand.
8. What is an sObject?
   - Standard or custom Salesforce data object.
9. Is Apex strongly typed?
   - Yes.
10. Is Apex object oriented?
    - Yes.

---

## Code-Oriented Questions

11. Why is the method static?
    - It can be called without creating an object.
12. Why use if-else for grade logic?
    - Simple conditional grading based on marks.
13. What is the output mechanism?
    - System.debug in logs.
14. Why call createStudent from showAll?
    - To reuse the grading logic.
15. Why use Integer for marks?
    - Marks are whole numbers.
16. What is the method return type?
    - void (no return value).
17. How is the code executed?
    - Via Execute Anonymous window.
18. What happens if marks is null?
    - It may cause a runtime exception.
19. How to view logs?
    - Open log and select Debug Only.
20. Where is the class stored?
    - In Apex Classes under Setup.

---

## Intermediate Questions

21. What is a governor limit?
    - Limits on resources to protect multi-tenant environment.
22. Why does Apex enforce limits?
    - To prevent one org from overusing resources.
23. What is a trigger?
    - Code that runs on data changes.
24. What is SOQL?
    - Salesforce Object Query Language.
25. What is DML in Apex?
    - Insert, update, delete operations on records.
26. When should you use Apex?
    - When no declarative tool can solve the problem.
27. Is Apex similar to Java?
    - Yes, syntax and structure are similar.
28. Can Apex call external APIs?
    - Yes, with callouts.
29. How are tests written in Apex?
    - Using test classes with @isTest.
30. Why is testing important in Apex?
    - Deployment requires minimum code coverage.

---

## Advanced and External Questions

31. What is the difference between Apex and Java?
    - Apex runs on Salesforce with governor limits.
32. Can Apex run asynchronously?
    - Yes, using future methods, queueable, batch.
33. What is the use of batch Apex?
    - Process large data in chunks.
34. What is Visualforce?
    - UI framework for Salesforce (legacy).
35. What is Lightning?
    - Modern UI framework for Salesforce.
36. What is multitenant architecture?
    - Multiple orgs share the same infrastructure.
37. Why should logic be bulkified?
    - To handle many records within limits.
38. Where does Apex code live?
    - Stored as metadata in Salesforce.
39. Can you access Apex outside Salesforce?
    - Only through API endpoints and integrations.
40. Why use Developer Edition?
    - Free environment for learning and practice.

---

## Quick Memory Sheet

- Apex = Java-like
- Debug = System.debug
- Run = Execute Anonymous
- Output = Debug Log
- Limits = Governor limits
