def ageCheck (age):
    print(f"your age is {age}")
    if age < 20:
        print("you are young")
    elif age == 20:
        print("congratuation!")
    else:
        print("adult")

ageCheck(19)
ageCheck(20)
ageCheck(30)