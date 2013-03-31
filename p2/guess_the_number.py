#!/usr/bin/python

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
# initialize global variables used in your code
secret = 0
new_game = False
count = 7

# define event handlers for control panel
print count    
def range100():
    # button that changes range to range [0,100) and restarts
    return

def range1000():
    # button that changes range to range [0,1000) and restarts
    return
    
def get_input(guess):
    # main game logic goes here 
    return

def input_guess(guess):
    # event handler that takes input guess
    global count
    count = count - 1
    if secret > guess:
        print "Higher :("
        print "You have", count, "guesses left..."
    elif secret < guess:
        print "Lower :("
        print "You have", count, "guesses left..."
    else:
        print "We have a winner!!"
        global new_game
        new_game = True
    
# create frame
def init():
    while True:
        global count
        print "Start new game..."
        count = 7
        global secret
        secret = random.randint(1,100)
        global new_game
        new_game = False
        while ~new_game:
            guess = int(raw_input())
            input_guess(guess)
            if count==0 and ~new_game:
                print "You fail!!"
                new_game = True


if __name__=="__main__":
    import sys
    #arg1 = int(sys.argv[1])
    init()


# register event handlers for control elements


# start frame


# always remember to check your completed program against the grading rubric

