# define the "factorial" function
def factorial(value):
    result = 1
    for n in range(value, 0, -1):
        result *= n

    return result


# Read keyboard for get the word
word = str(input("Write the word: ")).upper()

# Create the dictonary and the list
letters_count = {}
repetition = []

# Read the word to find each letter and its number
for letter in word:

    if letter not in letters_count:
        letters_count[letter] = 1

    else:
        letters_count[letter] += 1

# add repeated letters to "repetiton" list
for k, v in letters_count.items():
    if v > 1:
        repetition.append(v)

# Define the denominator
div = 1
for number in repetition:
    div *= factorial(number)

# Compute the anagrams number
final = factorial(len(word)) / div

# Display the number of anagrams
print(f"The total of permutations is: {final}")
