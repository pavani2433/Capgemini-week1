sorted_odds=lambda x:sorted(x)
numbers=[4,3,5,7,9,2,8]
list1=list(filter(lambda x:x%2!=0,numbers))
list2=list(map(lambda x:x*x if x%2==0 else x,numbers))
list1.sort()
list2.sort()
print(list1)
print(list2)