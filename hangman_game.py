# original Hangman with letter bug = selecting the same correct letter
#over and over will win the game

import random

answerlist = ["goose","swan","penguin","ostrich","eagle"]

random.shuffle(answerlist)

answer = list(answerlist[0])

#print(answer)
# empty list called display
display = []
# used  will contain all the  letters in the answer
# these will be taken away as the user guesses each one 
used= [] 

# extend will split the word into individual letter
# in the list eg yes becomes y,e,s
display.extend(answer)

# this copies the list of letters from display into 'used'
# this will enable us to work out if a letter has been used or not

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

incorrect = 5

# keep asking the user until all letters guessed
while count < len(answer) and incorrect >0:
    print("clue is the word based on birds")
    guess = input("please guess a letter: ")
    
    guess = guess.lower()
    print(count)
    
    # iterates through the letter in answer
    for i in range(len(answer)):
        # if the guessed letter matches a letter 
        # in the answer
        if answer[i] == guess and guess in used:
            # replace the index of the guess with
            # The actual letter they guessed
            display[i]= guess
            count = count + 1
            
            # print(used)
            used.remove(guess)
    if guess not in display:
        incorrect = incorrect - 1
        print("Sorry, wrong guess. you have",incorrect,"chance 1")

    print("you have guessed: ",count,"correct letter.")
    print("you have",incorrect,"chances left")
        
    # print out the new string with the guessed letters in
    print(' '.join(display))
    print()
if count == len(answer):
# once count is greater than length of word then :
    print("Well done, you guess the word")
else:
    print("Unfortunately you ran out of guess")
