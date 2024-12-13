import random

from hangman_words import data
from hangman_art import hangman


# pick random letter 
random_word=random.choice(data)
print(random_word)

random_word_range=len(random_word)

# Generate as many blanks as letters in word
random_word_blank=""
for letter in range(random_word_range):
    random_word_blank+="_"
print(random_word_blank)


lives=6
# Ask the user to guess a letter
word_after_replacement=""
while lives>1:
    guess_letter = input("Guess the letter: ")
    for letter in random_word:
        if letter==guess_letter:
            word_after_replacement+=guess_letter
        else:
            word_after_replacement+="_"
    print(word_after_replacement)

    lives -= 1
    print(hangman[lives])


print(word_after_replacement)








