import random 

# for hangman i have taken list of words which are to be guessed
words_list = ['apple', 'banana', 'carrot', 'dumplings', 'eggs', 'fish', 'gummies', 'horse', 'ice', 'jam', 'kiwi', 'lemone', 'mango', 'nemo', 'oranges','parrot']

#for each incorrect guess i will display some of the hangman figure
chances_to_guesses = {0:('..','',''),
                      1:('Ö',' ',' '), 
                      2:('Ö','|',' '), 
                      3:('Ö','/|',' '), 
                      4:('Ö','/|\\',' '),
                      5:('Ö','/|\\','/'), 
                      6:('Ö','/|\\','/\\')} 

#function to display the man 
def display_man(wrong_guesses): 
    print('\n***********************')
    for line in chances_to_guesses[wrong_guesses]: 
        print(line)
    print('***********************')

#function to display the hint 
def display_hint(hint): 
    print(' '.join(hint)) 

#function to display the correct answer wether you win or loose the game
def display_answer(answer): 
    print(' '.join(answer)) 

#function containg the main body of the program
def main():
    print('\n****** WELCOME TO HANGMAN GAME ******')
    while True:
        answer = random.choice(words_list) 
        hint = ['_'] * len(answer) 
        wrong_guesses = 0 
        guessed_letters = set() 
        is_running = True 

        while is_running:
            display_man(wrong_guesses) 
            display_hint(hint) 
            guess = input('\nEnter a letter:').lower() 
        
            if len(guess) != 1:  #checks if the guess is more than one character
                print('invalid input') 
                continue 
                
            if guess in answer: 
                for i in range(len(answer)):
                    if answer[i] == guess: 
                        hint[i] = guess 
            else:
                wrong_guesses += 1 

            if '_' not in hint: 
                display_answer(answer.upper()) 
                print('*****- CONGRATULATIONS YOU WON! -*****')
                is_running = False
                break

            elif wrong_guesses >= len(chances_to_guesses) - 1:  
                display_man(wrong_guesses) 
                print(f'The answer is {answer.upper()}') 
                print('*****- YOU LOSE THE GAME -*****')
                is_running = False
                break
        play_again = input("Play again? (y/n): ").lower()
        if play_again == 'n':
            break

                
main()
