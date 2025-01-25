n=int(input("Enter a number"))
option=input("Enter reverse to print reverse pettern")
if option=='reverse':
    for i in range(n,0,-1):
        print("*"*i)
else:
    for i in range(1,n+1):
        print("*"*i)