def grades(name,marks,perc):
    if perc>=75:
        print(f"Total marks scored by {name}={totalmarks}\npercentage={perc}\ngrade=A")
    elif perc<75 and perc>=65:
        print(f"Total marks scored by {name}={totalmarks}\npercentage={perc}\ngrade=B")
    elif perc<65 and perc>=55:
        print(f"Total marks scored by {name}={totalmarks}\npercentage={perc}\ngrade=C")
    else:
        print(f"Total marks scored by {name}={totalmarks}\npercentage={perc}\ngrade=Fail")

name=input("Enter student name")
totalmarks=0
for i in range(1,6):
    marks=int(input(f'Enter marks for subject {i}-'))
    totalmarks+=marks
perc=int((totalmarks/470)*100)
grades(name,totalmarks,perc)

