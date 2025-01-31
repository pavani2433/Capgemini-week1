products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
my_prod=products.split()
dict={}
for i in my_prod:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)