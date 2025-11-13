
text = input("Kehi mitho kura gara: ")

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
# for char, count in freq.items():
#     print(f"'{char}' ko frequency: {count}")
print(freq)