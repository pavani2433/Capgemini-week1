numbers=[2,2,4,6,3,4,6,1]
new_num=[]
for n in numbers:
    if n not in new_num:
        new_num.append(n)
print(new_num)