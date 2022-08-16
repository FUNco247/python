# define function in python 

# single
def sayHiTo(people):
    print("greeting")
    return print("hi " + people)

sayHiTo("FUNco") # hi FUNco

# func in func
def plus (a, b):
    return a + b

def mul (a, b):
    return a * b

def mulPlus (a, b, c):
    mul1 = mul(a,b)
    mul2 = mul(b,c)
    sum1 = mul1 + mul2
    return sum1

print(mulPlus(1,2,3))

# use variable like `` in JS

def intro (name, age):
    return f"my name is {name} and I'm {age} years old"

funco = intro("funco" , 32)

print(funco)