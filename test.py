from asyncio import FastChildWatcher


progress = True

while progress:
    print("this is plus machine")
    a= input("enter 1st number : ")
    b= input("enter 2nd number : ")
    c= int(a) + int(b)
    print(f"{a} plus {b} is {c} ")
    while True:
        again = input("plus again? please enter y / n : ")
        if again == "n":
            print("see you again")
            progress = False
            break
        elif again == "y":
            break
        else:
            print("should enter y (yes) or n (no)")

