num=int(input("Enter the number"))
rangelimit=int(input("Enter range"))
for i in range(1,rangelimit+1):
    result=num*i
    print(f'{num}*{i}={result}')