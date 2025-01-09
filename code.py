import random #we use random module here because we are choosing some random words in the list

# for hangman we need a set of words
words_list = ['apple', 'banana', 'carrot', 'dumplings', 'eggs', 'fish', 'gummies', 'horse', 'ice', 'jam', 'kiwi', 'lemone', 'mango', 'nemo', 'oranges','parrot']
choosen_word = random.choice(words_list) #to take the words randomly
print(choosen_word)

#for each wrong or incorrect guess i will display some ASCII art of the hangman
#so for that i need to have a dict with the key is number and value pair with the tuple () - to display some ascii art
chances_to_guesses = {0:(' ',' ',' '), #for no incorrect guesses ew dont display anything
                      1:('ö',' ',' '), #we display this for 1 incorrect guess
                      2:('ö','|',' '), #we display this for 2 incorrect guess
                      3:('ö','/|',' '), #we display this for 3 incorrect guess
                      4:('ö','/|\\',' '), #we display this for 4 incorrect guess
                      5:('ö','/|\\','/'), #we display this for 5 incorrect guess
                      6:('ö','/|\\','/\\')} #we display this for 6 incorrect guess
        
for line in chances_to_guesses[1]:
    print(line)
#function to display the man 
def display_man(wrong_guesses): #when we display the man we need to know the number of incorrect guesses to display the image
    pass
#function to display the hint 
def display_hint(hint) -> str: #we will have a hint as list with the underscore charaters. so that when the letter is right it will flip the underscore into the character
    pass
#function to display the correct answer wether you win or loose the game
def display_answer(answer):
    pass
#function containg the main body of the program
def main():
    pass
main()

