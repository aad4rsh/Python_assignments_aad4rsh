
size = int(input("Kati ota words cha? "))
words =[]

for i in range(size):
  word = input(f"{i+1} th term lekhnus: ")
  words.append(word)
print(words)

freq = {}
  
for w in words:
  if w in freq:
    freq[w] += 1
  else:
    freq[w] = 1

filtered ={}

for k,w in freq.items():
  if w > 1:
    filtered[k] = w
print(filtered)

  