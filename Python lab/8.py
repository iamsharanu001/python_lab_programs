# Python code to demonstrate naive method
# to compute factorial
n = int(input("enter a number::"))
fact = 1

for i in range(1, n+1):
	fact = fact * i

print(f"The factorial of {n} is : ", end="")
print(fact)
