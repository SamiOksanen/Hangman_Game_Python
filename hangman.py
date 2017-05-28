from failure import failed

word = 'asd'.upper()

def begin():
    play = input('Do you want to play a round of hangman guessing game (yes/no): ')
    if play == 'yes':
        game()
    elif play == 'no':
        print('Okey then. Good bye.')

def game():
    f = 0
    fill_word = '_' * len(word)
    print("Let's begin then!")
    while f < 9:
        print("Word: " + fill_word)
        letter = input('Please give a letter: ').upper()
        correct = 0
        for char in word:
            if char == letter:
                characters = list(fill_word)
                characters[word.index(char)] = letter
                fill_word = ''.join(characters)
                correct += 1
        if correct == 0:
            f += 1
            failed(f)
            if f >= 9:
                begin()
                break
        if fill_word == word:
            print('!!!YOU WIN, CONGRATULATIONS!!!')
            begin()
            break

begin()