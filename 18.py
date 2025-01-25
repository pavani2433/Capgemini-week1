weight=int(input("Enter weight "))
height=int(input("Enter height "))
BMI_value=weight/(height**2)
if BMI_value<10:
    print(f'BMI values is {BMI_value}, Underweight')
elif BMI_value>=10 and BMI_value<30:
    print(f'BMI values is {BMI_value}, Normal')
elif BMI_value>=30 and BMI_value<=50:
    print(f'BMI values is {BMI_value}, overweight')
else:
    print(f'BMI values is {BMI_value},obese')
