def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def bmi_status(bmi):
    if bmi < 25:
        return "Normal"
    else:
        return "Overweight"
    
weight = float(input("Weight (kg): "))
height = float(input("Height (sm): "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)

print(status)