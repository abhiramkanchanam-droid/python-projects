a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division, floor division, and modulus cannot be performed when the second number is 0")

print("Exponent:", a ** b)