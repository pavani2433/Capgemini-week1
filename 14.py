fac=1
num=int(input("Enter a number "))
if num<0:
    print("Error")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fac=fac*i
    print(f'Factorial of {num} is {fac}')