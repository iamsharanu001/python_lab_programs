# Take input from the user swapp two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping:")
print("First number =", num1)
print("Second number =", num2)

# Swapping logic
num1, num2 = num2, num1

print("After swapping:")
print("First number =", num1)
print("Second number =", num2)