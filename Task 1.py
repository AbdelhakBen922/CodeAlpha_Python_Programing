# importing random library for random word selection
import random

# creating a word list
with open('english.txt', 'r') as file:
    english_words_list = [line.strip() for line in file]


# a function that draws the hangman at a given stage (0-7)
def draw_hangman(stage):
    line_0 = ''
    line_1 = '    O'
    line_2 = '   /|\\'
    line_3 = '   / \\'
    line_4 = ''

    match stage:
        case 1:
            line_4 += ' ' * 6 + '==='
        case 2:
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='
        case 3:
            line_2 += ' |'
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='
        case 4:
            line_1 += '  |'
            line_2 += ' |'
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='
        case 5:
            line_0 += ' ' * 7 + '+'
            line_1 += '  |'
            line_2 += ' |'
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='
        case 6:
            line_0 += ' ' * 5 + '--+'
            line_1 += '  |'
            line_2 += ' |'
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='
        case 7:
            line_0 += ' ' * 4 + '+--+'
            line_1 += '  |'
            line_2 += ' |'
            line_3 += ' |'
            line_4 += ' ' * 6 + '==='

    print(line_0)
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)


# a function to display the word and check if the word is completely revealed
def word_display(word, letters_to_show):
    completed = True
    for letter in word:
        if letter in letters_to_show:
            print(letter, end='')
        else:
            print("_", end='')
            completed = False
    return completed


# the Game function
def Hangman(words_list):
    print("Welcome to Hangman Game:")
    answer = input("Do you want to play (y/n): ")

    if answer.lower() != 'y':
        print('Okay, Bye!')
        return

    chosen_word = random.choice(words_list)
    guessed_letters = []
    stage = 0
    completed = False

    while stage < 7:
        draw_hangman(stage)
        completed = word_display(chosen_word, guessed_letters)
        if completed:
            break

        guess = input('\nGuess a letter: ').lower()

        if guess in guessed_letters:
            print('You already chose this letter.')
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            stage += 1

    if completed:
        print('\nCongratulations, you won the game!')
    else:
        draw_hangman(7)
        print('Unfortunately, you lost.')
        print(f'The word was: {chosen_word}')


# testing the code
Hangman(english_words_list)
