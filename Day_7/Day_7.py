import random

word_list = ["tupac", "biggie", "wutang"]

chosen_word = random.choice(word_list)
print("(Cheat sheet: " + chosen_word + ")")

placeholder = ''
for letter in chosen_word:
    placeholder += " _ "
print(placeholder)

guessed_letters = ''
display = placeholder

while "_" in display:
    guess_letter = input("Guess a letter: ").lower()
    guessed_letters += guess_letter

    if guess_letter in chosen_word:
        print("Correct! '" + guess_letter + "' is in the word!")
    else:
        print("Wrong! '" + guess_letter + "' is not in the word!")

    display = ''
    for letter in chosen_word:
        if letter in guessed_letters:
            display += " " + letter + " "
        else:
            display += " _ "
    print(display)

print("You guessed the word: " + chosen_word)
