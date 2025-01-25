def celtofah(cel):
    return  ((9/5)*cel) + 32
def fahtocel(fah):
    return (fah-32) * 5/9
def keltocel(kel):
    return kel-273.15
def celtokel(cel):
     return cel+273.15
def keltofah(kel):
     return (kel-273.15) * 1.8 + 32
def fahtokel(fah):
    return (fah-32) *5 / 9 + 273.15
    
cel=int(input("Enter temperature to convert from celsius to fahrenheit"))
print(f'{celtofah(cel)} F')

cel=int(input("Enter temperature to convert from celsius to kelvin"))
print(f'{celtokel(cel)} K')

fah=int(input("Enter temperature to convert from fahrenheit to celsius"))
print(f'{fahtocel(fah)} C')

fah=int(input("Enter temperature to convert from fahrenheit to kelvin"))
print(f'{fahtokel(fah)} K')

kel=int(input("Enter temperature to convert from kelvin to fahrenheit"))
print(f'{keltofah(kel)} F')

kel=int(input("Enter temperature to convert from kelvin to celcius"))
print(f'{keltocel(kel)} C')
