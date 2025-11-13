text = input("Kehi mitho baat gara: ")

text_filt = text.replace(" ", "").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0

for char in text_filt:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowel haru ko sankhya: ", vowel_count)
print("Consonant haru ko sankhya: ", consonant_count)
    
