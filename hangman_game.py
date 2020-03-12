# original Hangman with letter bug = selecting the same correct letter over and over will win the game

import random

answerlist = ["word","look","hello","goodbye"]

random.shuffle(answerlist)

answer = list(answerlist[0])

#print(answer)
# empty list called display
display = []
# this will contain the used letters
used= [] 

# adds the variable answer to display
display.extend(answer)
# adds what is in display ie the answer to used
#so we can take letters out
used.extend(display)

#print(display)
# print(used)

# iterates through the list 'display'
for i in range (len(display)):
    # replace each index in the list with '_'
    display[i] = "_"

# the join command puts a space between each '_'
print(' '.join(display))
print()

# counter stops the game once all letters have been guessed
count =0

# keep asking the user until all letters guessed
while count < len(answer):
    guess = input("please guess a letter: ")
    guess = guess.lower()
    print(count)
    
    # iterates through the letter in answer
    for i in range(len(answer)):
        # if the guessed letter maches a letter 
        # in the answer
        if answer[i] == guess:
            # replace the index of the guess with
            # The actual letter they guessed
            display[i]= guess
            counter = count + 1
            
            # print(used)
            used.remove(guess)
    if guess not in display:
        print("Sorry, wrong guess")
        
    print("You have guessed: ",count,"correct letters.")
    # print out the new string with the guessed letters in
    print(' '.join(display))
    print()
    
print("Well done, you guess the word")