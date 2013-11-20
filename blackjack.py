# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user25_TaclO1CHfr_0.py

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# messages
DEAL_MESSAGE = "Deal again?"
MSG_ALREADY_IN_GAME = "You're already in game."
MSG_DEALER_WINS = "Dealer wins!"
MSG_PLAYER_WINS = "You win!"
MSG_BLACKJACK = "Blackjack"

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + " "

        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        for card in self.cards:
            if card.get_rank() == "A" and value + 10 <= 21:
                value += 10
            else:
                value += VALUES[card.get_rank()]

        return value

    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas, [pos[0] + (CARD_SIZE[0] * i) + 5, pos[1]])
            i += 1
        # draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s, r))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + " "

#define event handlers for buttons
def deal():
    global outcome, in_play, dealers_hand, players_hand, deck, score

    outcome = ""

    if not in_play:
        # your code goes here
        deck = Deck()

        dealers_hand = Hand()
        players_hand = Hand()

        dealers_hand.add_card(deck.deal_card())
        players_hand.add_card(deck.deal_card())
        dealers_hand.add_card(deck.deal_card())
        players_hand.add_card(deck.deal_card())

        print("DEALER'S HAND: " + str(dealers_hand))
        print("PLAYER'S HAND: " + str(players_hand))

        print("D_TOTAL: " +  str(dealers_hand.get_value()))
        print("P_TOTAL: " + str(players_hand.get_value()))
        in_play = True
    else: print(MSG_ALREADY_IN_GAME)

def hit():
    global players_hand, deck, in_play, score, outcome
    if in_play:
        if players_hand.get_value() <= 21:
            card = deck.deal_card()
            print(card)
            players_hand.add_card(card)

            if players_hand.get_value() > 21:
                print("P_TOTAL: " + str(players_hand.get_value()))
                print("You Have Busted!")
                print("\nDEALER WINS")
                outcome = "You have busted!"
                in_play = False
                score -= 1
                print ("SCORE: " + str(score))
            else:
                print("P_TOTAL: " + str(players_hand.get_value()))
                in_play = True
    else: print(DEAL_MESSAGE)
    # replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    global dealers_hand, players_hand, deck, in_play, score, outcome
    if not in_play:
        print(DEAL_MESSAGE)
    else:
        while dealers_hand.get_value() < 17:
            card = deck.deal_card()
            print(card)
            dealers_hand.add_card(card)
            print("D_TOTAL: " + str(dealers_hand.get_value()))
        if dealers_hand.get_value() > 21:
            print("Dealer has busted!")
            print("\nPLAYER WINS")
            outcome = "Dealer has busted!"
            score += 1
        else:
            if dealers_hand.get_value() >= players_hand.get_value():
                print("\nDEALER WINS")
                outcome = MSG_DEALER_WINS
                score -= 1
            else:
                print("\nPLAYER WINS")
                outcome = MSG_PLAYER_WINS
                score += 1

        print ("SCORE: " + str(score) + "\n")
        in_play = False
    # replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealers_hand.draw(canvas, [100, 200])
    players_hand.draw(canvas, [100, 300])
    canvas.draw_text(outcome, [300, 150], 32, "Blue", "sans-serif")
    canvas.draw_text(MSG_BLACKJACK, [10, 60], 72, "Black", "sans-serif")
    canvas.draw_text(str(score), [500, 60], 72, "White", "sans-serif")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [105 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
