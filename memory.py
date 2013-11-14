# implementation of card game - Memory
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

turns = 0

# helper function to initialize globals
def new_game():
    global cards, exposed, exposed_idxs, state, turns
    turns, state = 0, 0
    exposed_idxs = []
    exposed = [False for i in range(0,16)]
    cards = range(0,8) + range (0,8)
    label.set_text("Turns = " + str(turns))
    random.shuffle(cards)
     
# define event handlers
def mouseclick(pos):
    global cards,exposed, exposed_idxs, turns, state
    card_idx = (pos[0] // 50) + (pos[1] // 100) *8
    
    if not card_idx in exposed_idxs and not exposed[card_idx]: 
        if state == 0:
            state = 1
        elif state == 1:        
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if not cards[exposed_idxs[0]] == cards[exposed_idxs[1]]:  
                for i in exposed_idxs: exposed[i] = False
            state = 1        
            exposed_idxs = []  
        
        exposed_idxs.append(card_idx)
        exposed[card_idx] = True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    position = 0
    v_pos = 0
    for idx, card in enumerate(cards):
        v_pos = idx / 8
        canvas.draw_text(str(card), [position + 5, v_pos * 100 + 68], 72, "White", "monospace")
        if not exposed[idx]:
            canvas.draw_polygon([[position, v_pos * 100],[position+50, v_pos * 100],[position+50, v_pos * 100 + 100],[position,v_pos * 100 + 100]],4,"Black","Orange")
        if position < 350: position += 50
        else: position = 0

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 400, 200)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()