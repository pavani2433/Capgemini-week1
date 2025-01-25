def secondlargest(num):
    secondlargest=0
    largest=0
    for i in num:  
        if i > largest:
            secondlargest=largest
            largest=i
        elif i>secondlargest and i!=largest:
            secondlargest=i
    return secondlargest
numbers=input("Enter numbers ")
my_list=list(map(int,numbers.split()))
print(f'Second largest number is {secondlargest(my_list)}')
