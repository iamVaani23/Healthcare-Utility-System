import random
from collections import Counter

# 1. BMI Calculator
def bmi_calculator(wt, ht):
    # ht is expected in cm
    ht = ht / 100  
    bmi = wt / (ht ** 2)

    if bmi < 18.5:
        category = "Underweight: Consult a Doctor"
    elif bmi < 25:
        category = "Normal: you have a good overall health"
    elif bmi < 30:
        category = "Overweight: Consider lifestyle changes"
    else:
        category = "Obese: Consult a Doctor"

    # Instead of printing, return values
    return bmi, category

# 2. Symptom Checker
def symptom_checker(symptoms):
    results = []
    for symptom in symptoms:
        symptom = symptom.strip().lower()
        if symptom in ["fever", "cough", "cold", "sore throat"]:
            results.append(f"{symptom.title()} → Possible condition: Flu/Common Cold. Advice: Rest, fluids, consult doctor if severe.")
        elif symptom in ["headache", "dizziness", "blurred vision"]:
            results.append(f"{symptom.title()} → Possible condition: Migraine/Fatigue/Eye strain. Advice: Rest and seek medical help if persistent.")
        elif symptom in ["chest pain", "shortness of breath", "palpitations"]:
            results.append(f"{symptom.title()} → Possible condition: Heart/respiratory issue. Advice: Seek immediate medical attention!")
        elif symptom in ["stomach pain", "nausea", "vomiting", "diarrhea",'vomit']:
            results.append(f"{symptom.title()} → Possible condition: Food poisoning/stomach infection. Advice: Stay hydrated and consult doctor.")
        elif symptom in ["joint pain", "muscle ache", "swelling"]:
            results.append(f"{symptom.title()} → Possible condition: Arthritis/injury/infection. Advice: Rest and consult healthcare provider.")
        elif symptom in ["skin rash", "itching", "redness"]:
            results.append(f"{symptom.title()} → Possible condition: Allergy/skin infection. Advice: Avoid irritants and consult dermatologist.")
        elif symptom in ["fatigue", "weakness", "loss of appetite"]:
            results.append(f"{symptom.title()} → Possible condition: Nutritional deficiency/chronic illness. Advice: Balanced diet and medical check-up.")
        elif symptom in ["anxiety", "insomnia", "stress"]:
            results.append(f"{symptom.title()} → Possible condition: Mental health concern. Advice: Relaxation techniques and professional counseling.")
        else:
            results.append(f"{symptom.title()} → Symptom not recognized. Please consult a healthcare professional.")
    return results

# 3. Age Group Analyzer
def age_group_analyzer(ages):
    age_groups = []
    for age in ages:
        if age < 18:
            age_groups.append("Child")
        elif 18 <= age < 60:
            age_groups.append("Adult")
        else:
            age_groups.append("Senior")

    distribution = Counter(age_groups)
    return distribution

# 4. Appointment Token Generator

# Load used tokens from file (super simple)
used_tokens = set()
try:
    with open("tokens.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" - ")
            if len(parts) == 2:
                used_tokens.add(int(parts[1]))  # only token part
except:
    pass  # file doesn't exist yet


def generate_token_for(name):
    while True:
        token = random.randint(100000, 999999)

        if token not in used_tokens:
            used_tokens.add(token)

            # Save name and token in a very simple text format
            with open("tokens.txt", "a") as file:
                file.write(f"{name} - {token}\n")
            print("Saving tokens.txt in this folder:")

            return token




