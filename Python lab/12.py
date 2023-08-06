# Take input from the user
word = input("Enter a word: ")

# Initialize counters for letters and vowels
l_c = 0
v_c = 0

# Iterate over each character in the word
for char in word:
    # Check if the character is a letter
    if char.isalpha():
        l_c += 1
        # Check if the letter is a vowel
        if char.lower() in "aeiou":
            v_c += 1

# Print the number of letters and vowels
print("Number of letters:", l_c)
print("Number of vowels:", v_c)