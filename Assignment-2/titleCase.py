def title_case(words):
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    print("Title Case ma:", ' '.join(words))


text = input("Kehi mitho baat gara: ")
word = text.split()
title_case(word)