sal=int(input("Enter salary:"))
age=int(input("Enter age:"))
creditscore=int(input("Enter credit score"))
if sal>200000 and age<18 and creditscore>100000:
    print("Loan is rejected because you are not reaching the criteria")
elif sal>200000 or age<18 or creditscore>100000:
    if sal>200000:
        print("Loan is rejected because salary is high")
    elif age<18:
        print("Loan is rejected because you are under aged")
    elif creditscore>100000:
        print("Loan is rejected because creditscore is high")
else:
    print("Loan approved")
