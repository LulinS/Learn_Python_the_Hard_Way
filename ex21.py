def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b 

def divide(a, b):
    print (f"Dividing {a} / {b}")
    return a / b

print("Let's do some math")

age = add(20, 3)
height = subtract(185, 10)
weight = multiply(30, 2)
iq  = divide(400, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes {what}, can you do that by mind?")
