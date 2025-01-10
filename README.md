# Project-HANGMAN
Hangman is a classic word-guessing game.
The player tries to guess letters that they think might be in the word.
If the guessed letter is in the word, game continues until the word is completed.
If the guess is incorrect, a part of the hangman figure is displayed.
So, the game continues until the player either guesses the word correctly or exceeds the maximum number of incorrect guesses. 

# we use random module here because we are choosing some random words in the list
import random 
# for hangman i have taken list of words which are to be guessed
words_list = ['apple', 'banana', 'carrot', 'dumplings', 'eggs', 'fish', 'gummies', 'horse', 'ice', 'jam', 'kiwi', 'lemone', 'mango', 'nemo', 'oranges','parrot']
# for each wrong or incorrect guess i will display some of the hangman figure
# so for that i need to have a dict with the key is number and value pair with the tuple () - to display the figure
chances_to_guesses = {0:('..','',''), # for no incorrect guesses ew dont display anything
                      1:('Ö',' ',' '), # we display this for 1 incorrect guess
                      2:('Ö','|',' '), # we display this for 2 incorrect guess
                      3:('Ö','/|',' '), # we display this for 3 incorrect guess
                      4:('Ö','/|\\',' '), # we display this for 4 incorrect guess
                      5:('Ö','/|\\','/'), # we display this for 5 incorrect guess
                      6:('Ö','/|\\','/\\')} # we display this for 6 incorrect guess

# function to display the man 
def display_man(wrong_guesses): #when we display the man we need to know the number of incorrect guesses to display the image
    print('\n***********************')
    for line in chances_to_guesses[wrong_guesses]: # if the guess is wrong based on the number of wrong guesses it will retrieves the corresponding ASCII art from the chances_to_guesses dictionary.
        print(line)
    print('***********************')

# function to display the hint 
def display_hint(hint): #we will have a hint as list with the underscore charaters. so that when the letter is right it will flip the underscore into the character
    print(' '.join(hint)) #Joins the elements of the hint list with spaces and prints it

# function to display the correct answer wether you win or loose the game
def display_answer(answer): #takes the answers as input
    print(' '.join(answer)) #Joins the letters of the answer with spaces and prints it

# function containg the main body of the program
def main():
    print('\n****** WELCOME TO HANGMAN GAME ******')
    while True:
        answer = random.choice(words_list) 
        hint = ['_'] * len(answer) #to get the underscores for the words as hints
        wrong_guesses = 0 #created a variable to keep track for the no.of wrong guesses
        guessed_letters = set() #created an empty set to store the guessed letters
        is_running = True #created a boolen variable it is true as long as the game is running

        while is_running:
            display_man(wrong_guesses) 
            display_hint(hint) #called the function to display hint
            guess = input('\nEnter a letter:').lower() 
# if the player gives any words more than 1 letter
if len(guess) != 1: 
    print('invalid input') 
    continue 
# If the guessed letter is in the answer      
if guess in answer: 
    for i in range(len(answer)):
        if answer[i] == guess: 
            hint[i] = guess 
        else:
            wrong_guesses += 1 
            if '_' not in hint: #If there are no more underscores in the hint (all letters are guessed)
                display_answer(answer.upper()) #displays the correctc answer
                print('*****- CONGRATULATIONS YOU WON! -*****')
                is_running = False
                break
            elif wrong_guesses >= len(chances_to_guesses) - 1: #if the no.of wrong guesses exceeds the maximum limit 
                display_man(wrong_guesses) #displays the final hangman figure
                print(f'The answer is {answer.upper()}') #prints the  correct answer in upper case
                print('*****- YOU LOSE THE GAME -*****')
                is_running = False
                break
# to play again or not
play_again = input("Play again? (y/n): ").lower()
    if play_again == 'n':
        break

                
main()
