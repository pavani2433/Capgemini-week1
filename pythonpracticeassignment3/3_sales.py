sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
dict={}
for item in sales_data:
    region=item["region"]
    sales=item["sales"]
    if region not in dict:
        dict[region]=sales
    else:
        dict[region]+=sales
for region,sales in dict.items():
    print(region,sales)