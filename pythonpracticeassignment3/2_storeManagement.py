initial_stock = {"apple": 50,"banana": 100,"orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
dict={}
for item in initial_stock:
    dict[item]=initial_stock[item]-sold_item[item]
print(dict)