text = input("Kehi mitho baat gara: ")

word = text.split()

print(word)

for i in range(len(word)):
  if i % 2 == 1:
    word[i] = word[i][::-1]
print(" ".join(word))

