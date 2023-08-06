# Take input from the user multiplication table
num = int(input("Enter a number: "))

# Display multiplication table
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")