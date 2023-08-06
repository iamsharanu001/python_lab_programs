#Quadratic equation
import cmath

# Take input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find the solutions
s1 = (-b + cmath.sqrt(d)) / (2*a)
s2 = (-b - cmath.sqrt(d)) / (2*a)

# Print the solutions
print("The solutions are:")
print("x1 =", s1)
print("x2 =", s2)