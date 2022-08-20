import sys, pygame
import random
import math

pygame.init()

#size of screen
SIZE = width, height = 400,400
#radius of circle
RADIUS = 200
#colors
BLACK = 0, 0, 0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
GREY = 128,128,128
#text at the top left of the window
CAPTION_TEXT = "Estimating Pi!"
#font to be used to display pi estimate
FONT = pygame.font.Font("OpenSans-Regular.ttf", 20)

#list of all dots
dotInfoList = []

#total dots
total = 0

#number of dots inside the circle
circle = 0


while 1:
    #close when x is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #show the screen
    screen = pygame.display.set_mode(SIZE)

    #set the caption
    caption = pygame.display.set_caption(CAPTION_TEXT)

    #draw background circle
    backgroundCircle = pygame.draw.circle(screen, GREY, [width/2, height/2], RADIUS)

    #generate random dot position
    x = random.randint(0,400)
    y = random.randint(0,400)
    #distance the x of the dot is from the x of the center of the circle
    h = (x - 200)
    #distance the y of the dot is from the y of the center of the circle
    k = (y - 200)

    #default the color of the dot to red
    dotColor = RED

    #calculate distance from center of circle
    dist = math.sqrt((h*h)+(k*k))
    #change the color of the dot and add one to number of dots in circle to display and calculate pi
    if dist < RADIUS:
        circle += 1
        dotColor = GREEN
    #increase the total number of circles 
    total += 1

    #dot info for drawing the dot
    dotInfo = [x,y,dotColor]
    #add dot position and color to a list of dots to draw them
    dotInfoList.append(dotInfo)

    #draw current and previous dots
    for dotInfo in dotInfoList:
        #draw a dot with the color and position of the currently indexed dot info
        dotColor = dotInfo[2]
        dotPosition = [dotInfo[0],dotInfo[1]]
        pygame.draw.circle(screen,dotColor,dotPosition,1)
    
    #calculate pi
    result = 4 * (circle/total)
    
    #display the text
    text = FONT.render(str(result), True, WHITE)
    textRect = text.get_rect()
    textRect.bottomleft = (5,height)
    screen.blit(text,textRect)
    

    pygame.display.update()
    
    
    
