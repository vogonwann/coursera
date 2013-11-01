# http://www.codeskulptor.org/#user22_OxPObQ5qYeok26J_1.py
import simpleguitk as simplegui

# define global variables
counter = 0
attempts = 0
hits = 0
message = ""
score = ""
sucs_position = [0,0]
sucs_message = ""
sucs_color = ""
is_running = False

# Helper functions
def format(t):
    """ Converts time into formated string A:BC.D """
    # get tens
    tens = t % 10
    # get secs
    secs = ((t - tens) /  10) % 60
    # get mins    
    mins = ((t - tens) / 10) / 60
    
    secs_formated = add_leading_zero(secs)
    mins_formated = add_leading_zero(mins)
    
    return mins_formated + ":" + secs_formated + "." + str(tens)

def add_leading_zero(num):
    """ 
        Adds leading zero to a number 
        if that number is less than 10 
    """
    formated = ""
    if num <= 9:
        formated = "0" + str(num)
    else:
        formated = str(num)
    
    return formated

def format_score(att, hts):
    """ Formats the score label in x/y format"""
    return str(att) + "/" + str(hts)
    
def show_success_text(is_hit):
    """ Shows success text """
    global sucs_position, sucs_color, sucs_message
    if is_hit:
        sucs_position = [20, 235]
        sucs_color = "Yellow"
        sucs_message = "Hit!"
    else:
        sucs_position = [190, 235]
        sucs_color = "Red"
        sucs_message = "Miss! :("
        
# Event Handlers
def start():
    """ Start stopwatch """
    global is_running, sucs_message
    sucs_message = ""
    if not is_running:
        timer.start()
        is_running = True

def stop():    
    """ Stop stopwatch """
    global attempts, counter, hits, is_running
    is_hit = False
    timer.stop()
    if is_running:
        if (counter % 10) == 0:
            is_hit = True
            hits += 1
        show_success_text(is_hit)
        attempts += 1
    is_running = False

def reset():    
    """ Reset stopwatch and score """
    global timer, counter, message, attempts, hits, is_running, sucs_message
    timer.stop()
    is_running = False
    timer = simplegui.create_timer(100, tick)
    counter = 0
    attempts = 0
    hits = 0
    sucs_message = ""

# define event handler for timer with 0.1 sec interval
def tick():
    global counter, message
    counter += 1

# define draw handler
def draw(canvas):
    global message, score, attempts, hits
    message = format(counter)
    canvas.draw_polygon([[300, 0], [0, 0], [0, 35], [300, 35]], 1, '#2E2E2E', '#2E2E2E')
    canvas.draw_text(message, [80, 130], 48, "White")
    score = format_score(attempts, hits)
    canvas.draw_text(score, [230, 30], 32, "LightGray")
    canvas.draw_text(sucs_message, sucs_position, 32, sucs_color)

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 250)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()