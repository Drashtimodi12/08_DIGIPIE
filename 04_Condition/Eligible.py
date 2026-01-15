# Input age and check:
# If age < 18 → "Not eligible"
# If 18–24 → "Eligible for voting only"
# If age ≥ 25 → "Eligible for voting and driving"

age = int(input("Enter your age: "))
if age < 18:
    print("Not eligible.")
elif 18 <= age <= 24:
    print("Eligible for voting only.")
elif age >= 25:
    print("Eligible for voting and driving.")
else: 
    pass

# OP:
# Enter your age: 20
# Eligible for voting only.