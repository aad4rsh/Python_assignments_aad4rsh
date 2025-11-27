

def largest_word(sentence):

  max_len = 0
  for w in sentence:
      if len(w) > max_len:
        max_len = len(w)
        largest_word = w
  print("Deko text ma largest word:", largest_word)

text = input("Kehi mitho baat gara: ")
word = text.split()
largest_word(word)
