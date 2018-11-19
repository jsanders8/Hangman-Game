# Hangman Game by Jake Sanders
print("Hangman Game by JSanders | November 16, 2018\n")

# Open wordlist.txt so that we can access the words to choose from

word_list_file = open("wordlist.txt", "r")

# Create a local list of all of the words in wordlist.txt

word_list = word_list_file.readlines()

# Import random module to use for random word generator

from random import seed
from random import randint

# Random value generator
seed()
value = randint(0, len(word_list)-1)

# Using the random value as an index in the word list to pick a random word
raw_random_word = word_list[value]

# Putting the random word into str_random_word to display the random word for my own purposes while coding
str_random_word = raw_random_word[0:len(raw_random_word)-1]

# Putting the random word into a list so that it can be indexed
random_word = list(raw_random_word[0:len(raw_random_word)-1])
# print(str_random_word)
# print(len(random_word))

# Start of game sequence
print("Welcome to Hangman! A random word will be generated for you.")

# Set-up of the hidden word visual so that the player can see the length of the word and correct guesses
# hidden_word = list()
i = 0
space = " "
hidden_word = ["_"]*len(random_word)

# Setting the number of incorrect guesses allowed based on a choice of one of three difficulties by the user
incorrect_guesses = 0

while incorrect_guesses == 0:
    difficulty = input("Choose difficulty (easy, medium, or hard): ")
    if difficulty == "easy":
        incorrect_guesses = 9
    elif difficulty == "medium":
        incorrect_guesses = 6
    elif difficulty == "hard":
        incorrect_guesses = 3
    else:
        print("Please select a valid difficulty.")

print("You will receive " + str(incorrect_guesses) + " incorrect guesses.\n")

# Import ascii_lowercase in order to check validity of user guesses
from string import ascii_lowercase

# Initializing the guesses remaining to be the same as the difficulty defined allowable incorrect guesses.
guesses_left = incorrect_guesses

# Initializing an empty list to which each user guess will be added
all_guesses = list()

# Displaying the visual of the blanks for each unguessed letter
print(space.join(hidden_word))

# THIS IS THE PRIMARY LOGIC LOOP FOR THE GAME
while guesses_left > 0:
    guess = input("\nPlease guess a letter: \n")

    # Checking if the guess has already been guessed
    if guess in all_guesses:
        print("You have already guessed this letter.")
        continue

    # Checking that the guess is a string, that the guess is only one character long and that it is a lowercase letter
    if isinstance(guess, str) and len(guess) is 1 and guess in ascii_lowercase:
        all_guesses.append(guess)
        index = 0
        correct_guess = 0

        ''' The random word is now searched to see if the guess matches any letters. The initialized variable 'index' is
        set to 0 and is increased after each letter of the random word is checked to be the same as the guess. If the 
        guessed letter matches any letters in the random word, then the hidden word list is modified to add that letter
        to the correct spot. The correct_guess counter will also increment up for each matched letter in order to 
        identify whether to subtract a guess from guesses_left.  
        '''
        while index <= len(str_random_word):
            index = str_random_word.find(guess, index)
            if index != -1:
                hidden_word[index] = guess
                correct_guess += 1

            elif index == -1:
                if correct_guess == 0:
                    guesses_left -= 1
                break

            index += 1

        ''' After the random word has been searched for the guess input if the hidden word has bee modified to be the
        same as the random word then the user has correctly guessed all of the letters in the random word
        '''
        if hidden_word == random_word:
            print(space.join(hidden_word))
            print("\nYOU WIN!")
            break

        # Otherwise, the modified (or not) hidden word visual is displayed as well as guess information.
        print(space.join(hidden_word))
        print("\nYou have " + str(guesses_left) + " guesses remaining.")
        print("Letters guessed: " + " ".join(all_guesses))

    # If the guess did not meet the if statement criteria for a valid guess, then it will give instructions and return
    # to the top for another guess.
    else:
        print("Invalid guess. Enter only one lowercase letter at a time.")
        continue

if guesses_left == 0:
    print("\nYOU LOSE!")
