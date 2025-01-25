while True:
    userinput=input("Enter string or number to check for palindrome")
    if userinput==userinput[::-1]:
        print(f'{userinput} is palindrome')
    else:
        print(f'{userinput} is not palindrome')