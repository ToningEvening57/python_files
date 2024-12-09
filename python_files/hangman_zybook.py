import random
#import english_words_set
words = ['word1', 'word2', 'word3', 'word4', 'word5']
man = ['0','-','{','-','<']
choosen_word = random.choice(words)
def welcome():
    print('Welcome to Hangman!')

def board():
    print('_ _ _ _ _')
    print('Guess the word by inputting a letter!')
    print('Input: ', end='')
    check = input()
    letter_check(check)

#word_input = input

def letter_check(word):
    for letter in choosen_word:
        print(letter)
    if word == letter:
        print('True')
    else:
        print('False')
def drawing_man():
    print('0-{-<')
    #print(man)
def ending():
    if game_statement is true:
        print('You won!')
    else:
        print('You lose')

def random_word():
    print('Answer: ',end='')
    print(choosen_word)

welcome()
random_word()
drawing_man()
board()
