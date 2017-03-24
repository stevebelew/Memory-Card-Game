# implementation of card game - Memory

import simplegui
import random
CARD_WIDTH = 50
CARD_HEIGHT = 100
TOTAL_CARDS = 16
global turns
turns = 0

# helper function to initialize globals
def new_game():
    global state
    state = 0
    global turns
    turns = 0
    label.set_text("Turns: "+str(turns))
    global cards
    cards = []
    global choice_a
    global choice_b
    numbers = list(range(TOTAL_CARDS / 2) + range(TOTAL_CARDS / 2))
    random.shuffle(numbers)
    #print numbers
    for i in range(len(numbers)):
        cards.append([numbers[i],False,False])

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turns
    global choice_a
    global choice_b
    global state
    if state == 0 and cards[pos[0]//50][1] == False:
        #Expose card if no other card has been chosen
        cards[pos[0]//50][1] = True
        choice_a = cards[pos[0]//50]
        state += 1
        label.set_text("Turns: "+str(turns))
        return
    
    if state == 1 and cards[pos[0]//50] == choice_a:
            label.set_text("Turns: "+str(turns))
            return   
        
        #Expose card if only one other card has been chosen
       
    if state == 1 and cards[pos[0]//50] != choice_a:
        choice_b = cards[pos[0]//50]
        label.set_text("Turns: "+str(turns))
        choice_b[1] = True
        if choice_a[0]==choice_b[0]:
            choice_a[2] = True
            choice_b[2] = True
            state = 0
            turns += 1
            label.set_text("Turns: "+str(turns))
            choice_a = None
            choice_b = None
            return        
        else:
            turns += 1
            state = 2
            return
        
    if state == 2:
        choice_a[1] = False
        choice_b[1] = False
        choice_b = None
        choice_a = cards[pos[0]//50]
        cards[pos[0]//50][1] = True
        state = 1
        label.set_text("Turns: "+str(turns))
        return
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    x = CARD_WIDTH/2
    for i in range(len(cards)):        
        number = cards[i][0]
        if cards[i][1] == True or cards[i][2] == True:
            canvas.draw_text(str(cards[i][0]), (x, CARD_HEIGHT * 0.6), 25,'White' )
        else:
            canvas.draw_polygon([(i*CARD_WIDTH,0), (i*CARD_WIDTH + CARD_WIDTH,0), (i*CARD_WIDTH + CARD_WIDTH, CARD_HEIGHT), (i*CARD_WIDTH, CARD_HEIGHT)], 1, 'White','Green')

        x += CARD_WIDTH
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CARD_WIDTH * TOTAL_CARDS, CARD_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label(str(turns)) 

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
