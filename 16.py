inputnumbers=input("Enter numbers ")
my_list=list(map(int,inputnumbers.split()))
even_numbers=[]
odd_numbers=[]
for i in my_list:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f'Even numbers are {even_numbers}')
print(f'Odd numbers are {odd_numbers}')
