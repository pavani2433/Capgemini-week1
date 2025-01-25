def primeornot(num):
    if num==0 or num==1:
        print(f'{num} is not a prime number')
    else:
        for i in range(2,(num//2)+1):
            if num%i==0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
def rangenumbers(num1,num2):
    print(f'Prime numbers between {num1} and {num2} are')
    for i in range(num1,num2+1):
        primeornot(i)
num1=int(input("Enter a number 1 "))
num2=int(input("Enter a number 2 "))
primeornot(num1)
primeornot(num2)
rangenumbers(num1,num2)
