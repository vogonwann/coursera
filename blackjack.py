# Mini-project #6 - Blackjack ----
# http://www.codeskulptor.org/#user26_pq1IrU26LU_0.py

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite
CARD_SIZE = (73, 98)
CARD_SIZE_ = (125, 177)
CARD_CENTER = (62.5, 88.5)
card_images = simplegui.load_image("http://i.imgur.com/Mn3ONv1.jpg")

# load card back
CARD_BACK_SIZE = (73, 98)
CARD_BACK_SIZE_ = (125, 177)
CARD_BACK_CENTER = (62.5, 88.5)
card_back = simplegui.load_image("http://i.imgur.com/8ionrg6.jpg")

# load bground image
background_image = simplegui.load_image("http://i.imgur.com/N9ka4dG.jpg")

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
MSG_PLAYER_LOOSES = "You lose!"
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
        card_loc = (CARD_CENTER[0] + CARD_SIZE_[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE_[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE_, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

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

        in_play = True
    else:
        outcome = MSG_PLAYER_LOOSES
        score -= 1
        in_play = False
def hit():
    global players_hand, deck, in_play, score, outcome
    if in_play:
        if players_hand.get_value() <= 21:
            card = deck.deal_card()
            players_hand.add_card(card)

            if players_hand.get_value() > 21:
                outcome = "You have busted!"
                in_play = False
                score -= 1
            else:
                in_play = True
    else: outcome = DEAL_MESSAGE

def stand():
    global dealers_hand, players_hand, deck, in_play, score, outcome
    if not in_play:
        outcome = DEAL_MESSAGE
    else:
        while dealers_hand.get_value() < 17:
            card = deck.deal_card()
            dealers_hand.add_card(card)
        if dealers_hand.get_value() > 21:
            outcome = "Dealer has busted!"
            score += 1
        else:
            if dealers_hand.get_value() >= players_hand.get_value():
                outcome = MSG_DEALER_WINS
                score -= 1
            else:
                outcome = MSG_PLAYER_WINS
                score += 1
        in_play = False

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_image(background_image, [600,600], [1200,1200], [300,300], [600,600])
    canvas.draw_text("Dealer:", [80, 230], 20, "White", "sans-serif")
    dealers_hand.draw(canvas, [50, 200])
    canvas.draw_text("Player:", [80, 380], 20, "White", "sans-serif")
    players_hand.draw(canvas, [50, 350])
    canvas.draw_text(outcome, [400, 230], 20, "White", "sans-serif")
    #canvas.draw_text(MSG_BLACKJACK, [10, 60], 72, "Black", "sans-serif")
    canvas.draw_text("Score:", [400, 520], 32, "White", "sans-serif")
    canvas.draw_text(str(score), [500, 520], 32, "White", "sans-serif")
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE_, [55 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

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
