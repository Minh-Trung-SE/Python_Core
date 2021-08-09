def bmi_calculator(weight, height):
    result_bmi = weight / (height * 2)
    return result_bmi


def bmi_infor(weight, height):
    bmi = bmi_calculator(weight, height)
    if bmi < 18.5:
        print("UNDERWEIGHT")
    if bmi >= 18.5 and bmi <= 24.9:
        print("NORMAL")
    if bmi >= 25 and bmi <= 29.9:
        print("OVERWEIGHT")
    if bmi >= 30 and bmi <= 34.9:
        print("OBESE")
    if bmi > 35:
        print("EXTREMLY OBESE")
