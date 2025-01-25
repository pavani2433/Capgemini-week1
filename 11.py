password=input("Enter a password")
uppercase=0
lowercase=0
digit=0
specialchar=0
for i in password:
    if i>='a' and i<='z':
        lowercase+=1
    elif i>='A' and i<='Z':
        uppercase+=1
    elif i.isdigit():
        digit+=1
    elif i!=" ":
        specialchar+=1
if len(password)>=8 and lowercase>0 and uppercase>0 and digit>0 and specialchar>0:
    print(f"{password} is strong")
else:
    print(f'{password} is not strong')
