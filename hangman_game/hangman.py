import random


def loadWord():
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord

def start_game(secretWord):
    print("\n\t\t\tWELCOME TO HANGMAN\n")
    print("Let's see if you can guess the secret word? Hint: I't has %i letters in it" % len(secretWord))
    black_word_array = []
    for e in secretWord:
        black_word_array.append("_")

    print(black_word_array)


def guess(secretWord, guessedCorrectly):
    numberofguesses = len(secretWord)

    for e in secretWord:
        letter = input("Guess a letter: ")

        if letter in secretWord:
            guessedCorrectly.append(letter)
            numberofguesses -= 1
            print("%s\n%i guesses left\n" % (putlettersInOrder(secretWord, guessedCorrectly), numberofguesses))
        else:
            guessedCorrectly.append("_")
            numberofguesses -= 1
            print("%s\n%i guesses left\n" % (putlettersInOrder(secretWord, guessedCorrectly), numberofguesses))


    return guessedCorrectly


def putlettersInOrder(secretWord, guessedCorrectly):
    new_array = []
    for l in secretWord:
        if l in guessedCorrectly:
            new_array.append(l)
        else:
            new_array.append("_")
    return new_array

def isWordGuessed(word_array):
    word = ""
    for l in word_array:
        word += l

    if word == secretWord:
        return True
    else:
        return False


if __name__ == '__main__':
    secretWord = loadWord()
    print(secretWord)

    secret_array = []
    for a in secretWord:
        secret_array.append(a)

    start_game(secretWord)
    correct = []

    guess(secretWord, correct)
    word_array = putlettersInOrder(secretWord, correct)

    if isWordGuessed(word_array):
        print("Nice, you guessed it!")
    else:
        print("Sorry, the secret word is %s" % secretWord)
