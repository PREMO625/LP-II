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


    # Ask fever symptom
    @Rule(Fact(action="diagnose"), NOT(Fact(fever=W())))
    def ask_fever(self):
        self._ask("Do you have fever? ", "fever")


    # Ask cough symptom
    @Rule(Fact(action="diagnose"), NOT(Fact(cough=W())))
    def ask_cough(self):
        self._ask("Do you have cough? ", "cough")


    # Ask headache symptom
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


    # Rule for Flu
    @Rule(
        Fact(fever="yes"),
        Fact(cough="yes"),
        Fact(headache="yes"),
        Fact(body_ache="yes"),
    )
    def flu(self):
        print("\nPossible Disease : Flu")
        print("Treatment : Take rest, drink fluids, and consult doctor.")


    # Rule for Common Cold
    @Rule(
        Fact(fever="no"),
        Fact(cough="yes"),
        Fact(sore_throat="yes"),
        Fact(headache="no"),
    )
    def cold(self):
        print("\nPossible Disease : Common Cold")
        print("Treatment : Steam inhalation and proper rest.")


    # Rule for Migraine
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