# Function to calculate the GCD (Euclidean algorithm)
def c_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the LCM
def c_lcm(a, b):
    gcd = c_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the GCD
gcd = c_gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", gcd)

# Calculate and display the LCM
lcm = c_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)