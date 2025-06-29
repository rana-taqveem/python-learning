
import random

stages = ['''
  +-----+
  |
  |
  |
  |
  |
  |
  |
  |
====== ''',
'''
  +-----+
  |     |
  |
  |
  |
  |
  |
  |
  |
====== ''',
'''
  +-----+
  |     |
  |     |
  |
  |
  |
  |
  |
  |
====== ''',
'''
  +-----+
  |     |
  |     |
  |     O
  |
  |
  |
  |
  |
====== ''',
'''
  +-----+
  |     |
  |     |
  |     O
  |     |
  |
  |
  |
  |
====== ''',
'''
  +-----+---
  |     |
  |     |
  |     O
  |    /|
  |
  |
  |
  |
====== ''',
'''
  +-----+---
  |     |
  |     |
  |     0
  |    /|\\
  |
  |
  |
  |
====== ''']

print(f' \n\n -----  Welcome to Hangman -----\n')
print(f' Lets guess the letters of a word to save the man \n')
total_lives = 6
lives_used = 0

word_list = ['abject', 'acetic', 'agouti', 'ajijic', 'anoxia', 'arroyo', 'aufeis', 'aumbry', 'avatar', 'basalt', 'bathos', 'burgle', 'caliga', 'callow', 'castle', 'chador', 'chaise', 'chrism', 'clutch', 'coccyx', 'coulee', 'crulge', 'dactyl', 'degust', 'dengue', 'diadem', 'dikdik', 'eocene', 'eryops', 'ewerer', 'feeble', 'flapse', 'gerbil', 'gneiss', 'gnomic', 'googly', 'gravid', 'guitar', 'hansom', 'harbor', 'indigo', 'jerboa', 'lappet', 'lhotse', 'lizard', 'miacid', 'miasma', 'mohawk', 'mothra', 'nettly', 'ocelot', 'onager', 'orchil', 'ornery', 'orrery', 'ovular', 'panzer', 'pilfer', 'poncho', 'proton', 'python', 'quagga', 'quahog', 'quorum', 'quotha', 'remuda', 'rugose', 'schism', 'schist', 'shtetl', 'slithy', 'snazzy', 'sphere', 'spinet', 'spleen', 'stigma', 'sulfur', 'tattoo', 'tupelo', 'tureen', 'twelve', 'twibil', 'umlaut', 'vellus', 'velvet', 'virago', 'walrus', 'wapiti', 'whinge', 'xystis', 'zamler']
word = random.choice(word_list)

guessed_list = ['_'] * len(word)
guessed_word = ' '.join(guessed_list)
print(stages[0])

while True:
    
    print(f'\nWord to guess: {guessed_word}')
    guessed_letter = input('Guess a letter: ')

    found = False
    for i, char in enumerate(word):
        if guessed_letter == char:
            found = True
            guessed_list[i] = f'{guessed_letter}'

    
    guessed_word = ''.join(guessed_list)

    if not found:
        lives_used = lives_used + 1
        print(f"You guessed {guessed_letter}, that is not in the word. You lose a life. \n")
        print(stages[lives_used])
        print('  ')
        print(f"************************** {total_lives-lives_used}/{total_lives} LIVES LEFT ********************************")

        if lives_used == total_lives:
            print("You Lost!")
            break
    else:
        print('  ')
        print(stages[lives_used])
        result_string = ''.join(guessed_list)
        if result_string.replace(" ","") == word:
            print("You Won!")
            break


