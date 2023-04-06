def factorial(value):
    result = 1
    for n in range(value, 0, -1):
        result *= n

    return result


word = str(input("Write the word: ")).upper()
letters_count = {}
repetition = []

for l in word:

    if l not in letters_count:
        letters_count[l] = 1

    else:
        letters_count[l] += 1

for k, v in letters_count.items():
    if v > 1:
        repetition.append(v)

div = 1
for number in repetition:
    div *= factorial(number)

final = factorial(len(word)) / div
print(f"The total of permutations is: {final}")
