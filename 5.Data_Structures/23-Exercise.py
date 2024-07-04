from pprint import pprint
# My solution
sentence = "This is a common interview question"
sentence = sentence.lower()
counts = {}

for char in sentence:
    if char != " ":
        if counts.get(char) is None:
            counts[char] = 1
        else:
            counts[char] = counts.get(char) + 1

print(counts)
qtd = -1
most_common = ""

for key in counts:
    if qtd == -1:
        most_common = key
        qtd = counts[key]
    else:
        if counts[key] > qtd:
            most_common = key
            qtd = counts[key]
        elif counts[key] == qtd:
            most_common = (f"{most_common}, {key}")

print(f"The letter that repetes the most is {most_common}")


# Solution of Mosh

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)

char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print(char_frequency_sorted[0])

print((char_frequency.items()))
