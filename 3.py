import random
def guessthenumber():
    numbertoguess = random.randint(1, 100)
    att= 0
    while True:
        guess=int(input("Enter your guess number:"))
        att=att+1
        if guess<numbertoguess:
            print("Too Low! Try again")
        elif guess>numbertoguess:
            print("Too High! Try again")
        else:
            print(f"Congratulations! You have guessed the number correctly in {att} attempts.")
            break
guessthenumber()
