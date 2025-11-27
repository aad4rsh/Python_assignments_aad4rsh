text = input("Kehi mitho baat gara: ")
word = text.split()

freq = {}

for w in word:
  if w in freq:
    freq[w] += 1
  else:
    freq[w] = 1
print("Words haruko frequency")
print(freq)