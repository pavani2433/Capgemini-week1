products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
# prod=list(map(lambda x: x['price']*0.8 if x['price']>100 else x['price'],products))
# print(prod)
prod1=list(filter(lambda x:x['price']>100,products))
print(prod1)
res=list(map(lambda x:x['name'],prod1))
print(res)