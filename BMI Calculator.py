# BMI Calculator with Categories

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
result = calculate_bmi(weight, height)

# Determine BMI category
category = bmi_category(result)

# Display the result
print(f"Your BMI is: {result:.2f}")
print(f"You are categorized as: {category}")