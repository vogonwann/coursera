# http://www.codeskulptor.org/#user21_SZaRsbLoc5D00rY_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simpleguitk as simplegui


# initialize global variables used in your code
secret_number = 0
max_guesses = 7
max_range = 100
left_guesses = 0


# helper function to start and restart the game
def new_game():
    """Initialize new game"""
    global secret_number, max_guesses, left_guesses, max_range

    print("New game started!\n")

    # Compute max number of guesses
    max_guesses = int(math.ceil(math.log(max_range + 1, 2)))
    left_guesses = max_guesses

    if max_guesses == 7:
        print "Range is (0-100]"
        secret_number = random.randrange(0, 100)
    else:
        print "Range is (0-1000]"
        secret_number = random.randrange(0, 1000)

    print("Maximum no. of guesses: " + str(max_guesses))
    print("Guesses left: " + str(left_guesses) + "\n")


# define event handlers for control panel
def range100():
    """Sets the range from 0 to 100, excluding 100"""
    global max_range, left_guesses
    max_range = 100
    left_guesses = 7

    new_game()


def range1000():
    """Sets the range from 0 to 1000, excluding 1000"""
    global max_range, left_guesses
    max_range = 1000
    left_guesses = 10

    new_game()


def input_guess(guess):
    """Main game logic"""
    global left_guesses, max_range

    print "Guess was: " + guess
    left_guesses -= 1
    print "Guesses left: " + str(left_guesses)

    try:
        if 0 > guess > max_range:
            print "Guess is out of range!"
        else:
            if left_guesses > 0:
                if int(guess) < secret_number:
                    print "Higher!"
                elif int(guess) > secret_number:
                    print "Lower!"
                else:
                    print "Correct!\n"
                    new_game()
            else:
                print "You loose! Correct number was: " + str(secret_number) + "\n"
                new_game()
    except Exception, e:
        print "Error: " + e.message

    print ""

# create frame
frame = simplegui.create_frame("Guess the number", 200, 150)


# register event handlers for control elements
frame.add_button("Range (0, 100]", range100, 200)
frame.add_button("Range (0, 1000]", range1000, 200)
frame.add_input("Guess", input_guess, 200)


# call new_game and start frame
frame.start()
new_game()
