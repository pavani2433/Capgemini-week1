dict={}
def add_items(item,price):
    dict[item]=price
def view_cart():
    print(dict)
def exit():
    print("exit")
def total_price():
    sum=0
    for item in dict:
        sum+=dict[item]
    print(f"total price is:{sum}")
numop=int(input("enter no.of operations"))

for j in range(numop):
     op=input("enter the operation")
     if(op=="add"):
        n=int(input("no.of items to add"))
        for i in range(n):
            item=input("item")
            price=int(input("price"))
            add_items(item,price)
     elif(op=="view"):
         view_cart()

     elif(op=="total price"):
         total_price()

     elif(op=="exit"):
           exit()
     else:
         print("invalid")