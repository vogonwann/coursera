import random

def number_to_name(number):
    """
    Converts number to name
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print('Number is not in correct range!')


def name_to_number(name):
    """
    Converts name to number
    """
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print('Not a correct name!')


def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    # Handle player's wrong choice
    # Player number will be 'None' if name is wrong
    if player_number is not None:
        print('Player chooses ' + number_to_name(player_number))
        print('Computer chooses ' + number_to_name(comp_number))

        result = (player_number - comp_number) % 5

        if (result == 1) or (result == 2):
            print('Player wins!\n')
        if (result == 3) or (result == 4):
            print('Computer wins!\n')
        elif result == 0:
            print('Player and computer tie!\n')
    else:
        print("Wrong choice! Player: " + name + "\n")

# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

