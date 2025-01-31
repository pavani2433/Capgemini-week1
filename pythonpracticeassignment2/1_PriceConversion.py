#price conversion
def conversion():
    priceslist_inr =[3000,56000,45000,2300]
    result=map(lambda x:x*0.012,priceslist_inr)
    print(list(result))
    result2=map(lambda x:f'{x*0.011:.2f}',priceslist_inr)
    print(list(result2))
conversion()