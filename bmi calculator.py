def calculate_bmi(weight, height):
    return (weight * 703) / (height ** 2)


def determine_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normalweight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
    
while True:
    try:
        height = float(input("Enter your height in inches: "))
        weight = float(input("Enter your weight: "))

        if height <= 0 or weight <= 0:
            raise ValueError("height and weight must be positive numbers.")

        bmi_result = calculate_bmi(weight, height)
        category_result = determine_category(bmi_result)

        print(f"Your BMI is: {bmi_result:.4f}")
        print(f"Your Category is {category_result}")

        break

    except ValueError as e:
        print(f"Error: {e}.Enter valid values for height and weight.")
