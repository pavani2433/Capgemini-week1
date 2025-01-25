string=input("Enter the string")
vowelcount=0
consonantcount=0
digitcount=0
specialcharactercount=0
vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
for i in string:
    if i in vowels:
        vowelcount+=1
    elif i in consonants:
        consonantcount+=1
    elif i.isdigit():
        digitcount+=1
    elif not i.isalnum() and i!=" ":
        specialcharactercount+=1
print(f'Vowels={vowelcount}\nConsonants={consonantcount}\nDigit{digitcount}\nSpecialcharacters={specialcharactercount}')
print(string[::-1])
    