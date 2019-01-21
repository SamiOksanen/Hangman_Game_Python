from failure import failed
from word_list import words
from random import randrange

def begin():
    while True:
        play = input('Do you want to play a round of hangman guessing game (yes/no): \n')
        if play == 'yes' or play == 'YES' or play == 'y':
            print('Themes: ')
            for key in sorted(words.keys()):
                print(key)
            while True:
                choose = input('Please choose a theme: \n').lower()
                if choose in words:
                    x = randrange(len(words[choose]))
                    word = words[choose][x].upper()
                    game(word)
                    break
                else:
                    print("We don't have {} theme".format(choose))
            break
        elif play == 'no' or play == 'NO' or play == 'n':
            print('Okey then. Good bye.')
            break
        else:
            print('Please answer correctly')

def game(word):
    f = 0
    fill_word = '_' * len(word)
    for i in range(len(word)):
        if ' ' == word[i]:
            characters = list(fill_word)
            characters[i] = ' '
            fill_word = ''.join(characters)
    print("Let's begin then!")
    while f < 9:
        print(str(fill_word.count("_")) + " empty letters")
        print("Word: " + fill_word)
        while True:
            letter = input('Please give a letter: \n').upper()
            if 1 <len(letter) > 1:
                print('Please give only one letter')
            elif letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ -.,':
                print('Please give one of these letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ -.,')
            else:
                break
        correct = 0
        for i in range(len(word)):
            if letter == word[i]:
                characters = list(fill_word)
                characters[i] = letter
                fill_word = ''.join(characters)
                correct += 1
        if correct == 0:
            f += 1
            failed(f)
            if f >= 9:
                begin()
                break
        if fill_word == word:
            print("Word: " + fill_word)
            print('!!!YOU WIN, CONGRATULATIONS!!!')
            begin()
            break

begin()
