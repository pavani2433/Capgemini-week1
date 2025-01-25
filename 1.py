balance=1000
def checkbalance():
        print(f"Availaible balance in your account is {balance}")
def depositmoney(dep):
        global balance
        balance=balance+dep
        print(f"{dep} has been deposited into your account, your balance is {balance}")
def withdrawmoney(withdraw):
    if withdraw<=balance:
        print(f'You have withdrawn {withdraw}, {balance-withdraw} is available in your account')
    else:
         print(f"Insufficient balance")
def exit():
    print("Exited")
checkbalance()
dep=int(input("Enter money you want to deposit"))
depositmoney(dep)
withdraw=int(input("Enter money you need to withdraw"))
withdrawmoney(withdraw)
exit()