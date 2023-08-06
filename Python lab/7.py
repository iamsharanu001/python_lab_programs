# Take input from the user prime numbers
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)