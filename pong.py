# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user23_bznNa4hUU8_1.py

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDLE_SPEED_INC = 3
BALL_SPEED_INC = 1.1
SCORE_FONT_SIZE = 80

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_vel = [0, 0]
    ball_pos = [0, 0]

    ball_pos = [WIDTH / 2, HEIGHT/2]

    # Randomize initial velocity
    ball_vel[0] = 10 + random.randrange(120, 240) / 60
    ball_vel[1] = -(10 + random.randrange(60, 180) / 60) # Make sure that the ball goes up
    # Apply direction to the ball
    if not direction:
        # ball goes left
        ball_vel[0] = -ball_vel[0]


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_pos = HEIGHT / 2 + HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 + HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

    # Randomize horizontal direction of the ball
    dirc = random.randrange(0,11)

    if dirc % 2 == 0: spawn_ball(LEFT)
    else: spawn_ball(RIGHT)

def draw_middle_line(canvas, p1, p2, width, color):
    i = 0
    delta = 25
    chunk_length = 15
    for p in range(p1[1], p2[1] + delta):
        canvas.draw_line([p1[0], p + i], [p2[0], p + i + 15], width, color)
        i += delta

# define event handlers
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

    # draw mid line and gutters
    # c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    draw_middle_line(c, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 8, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    # detect ball collision with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # detect ball collision with gutters
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        #left gutter
        if paddle1_pos - PAD_HEIGHT <= ball_pos[1] <= paddle1_pos:
            #collided with left paddel
            ball_vel[:] = [bv * BALL_SPEED_INC for bv in ball_vel]
            ball_vel[0] = - ball_vel[0]
        else:
            #score player 2
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        #right gutter
        if paddle2_pos - PAD_HEIGHT <= ball_pos[1] <= paddle2_pos:
            #collided with right paddel
            ball_vel[:] = [bv * BALL_SPEED_INC for bv in ball_vel]
            ball_vel[0] = - ball_vel[0]
        else:
            #score player 1
            score1 += 1
            spawn_ball(LEFT)

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    c.draw_circle(ball_pos, 20, 1, "White", "White")

    # detect if paddles are in field boundaries
    if not (paddle1_pos - PAD_HEIGHT + paddle1_vel <= 0 or paddle1_pos + paddle1_vel >= HEIGHT):
        paddle1_pos += paddle1_vel

    if not (paddle2_pos - PAD_HEIGHT + paddle2_vel <= 0 or paddle2_pos + paddle2_vel >= HEIGHT):
        paddle2_pos += paddle2_vel

    # draw paddles
    c.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos - PAD_HEIGHT], [0, paddle1_pos - PAD_HEIGHT]], 1, "White", "White")
    c.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos - PAD_HEIGHT], [WIDTH, paddle2_pos - PAD_HEIGHT]], 1, "White", "White")

    # draw score
    score1_posx = WIDTH / 2 - (100 + (len(str(score1)) * SCORE_FONT_SIZE / 2))
    score2_posx = WIDTH / 2 + (100 - ((len(str(score2)) -1) * SCORE_FONT_SIZE / 2))

    c.draw_text(str(score1), [score1_posx, 75], 80, "White", 'monospaced')
    c.draw_text(str(score2), [score2_posx, 75], 80, "White", 'monospaced')

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += PADDLE_SPEED_INC
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= PADDLE_SPEED_INC
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += PADDLE_SPEED_INC
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= PADDLE_SPEED_INC

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 200)

# start frame
new_game()
frame.start()