#Pi estimation using Python and pyGame by Tyler Knudtson
#Inspiration by Code Train https://youtu.be/5cNnf_7e92Q

import sys,pygame,random,math

pygame.init()

#size of screen
SIZE = WIDTH, HEIGHT = 400,400

#radius of circle
RADIUS = 200

#All Colors found by googling "rgb color picker"
BLACK = 0, 0, 0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
GREY = 128,128,128
LIGHT_GREY = 217, 217, 217
DARK_GREY = 56, 56, 56
LIGHT_BLUE = 3, 236, 252
PURPLE = 165, 3, 252
ORANGE = 252, 132, 3
YELLOW = 252, 248, 3

#text at the top left of the window
CAPTION_TEXT = "Estimating Pi!"

DRAW_ALL_DOTS_BUTTON_TEXT = "Draw All Dots"
DRAW_ALL_DOTS_BUTTON_CENTER = (WIDTH/2, HEIGHT/2-50)

DRAW_CURRENT_DOT_BUTTON_TEXT = "Draw Only Current Dot"
DRAW_CURRENT_DOT_BUTTON_CENTER = (WIDTH/2, HEIGHT/2+50)

BACK_BUTTON_TEXT = "Back"
BACK_BUTTON_CENTER = (25,20)

TITLE_BUTTON_ONE_TEXT = "Estimating Pi with Python"
TITLE_BUTTON_ONE_CENTER = (WIDTH/2,20)

TITLE_BUTTON_TWO_TEXT = "by Tyler Knudtson 2022"
TITLE_BUTTON_TWO_CENTER = (WIDTH/2,47)

#font to be used to display pi estimate
FONT = pygame.font.Font("OpenSans-Regular.ttf", 20)

#list of all dots
dotInfoList = []

#total dots
totalDots = 0

#number of dots inside the circle
circleDots = 0

#draws a button given a string, tuple, and 2 colors
#returns the rectangle of the button
def drawAButton(text,center,textColor,bgColor):
    text = FONT.render(text, True, textColor,bgColor)
    textRect = text.get_rect()
    textRect.center = (center)
    screen.blit(text,textRect)

    return textRect

#default values to make sure it doesn't blow up
menu = 0
drawAllDots = True

while 1:
    #show the screen
    screen = pygame.display.set_mode(SIZE)

    #determine which screen to render either menu or
    if menu == 0:
        #draw the dot selection buttons
        drawAllDotsButtonRect = drawAButton(DRAW_ALL_DOTS_BUTTON_TEXT, DRAW_ALL_DOTS_BUTTON_CENTER,WHITE,GREY)
        drawCurrentDotButtonRect = drawAButton(DRAW_CURRENT_DOT_BUTTON_TEXT,DRAW_CURRENT_DOT_BUTTON_CENTER,WHITE,GREY)

        #draw the title buttons
        button4Rect = drawAButton(TITLE_BUTTON_ONE_TEXT, TITLE_BUTTON_ONE_CENTER,GREEN,DARK_GREY)
        button5Rect = drawAButton(TITLE_BUTTON_TWO_TEXT,TITLE_BUTTON_TWO_CENTER,GREEN,DARK_GREY)

        #change color of the selection buttons if you mouse over them
        if drawAllDotsButtonRect.collidepoint(pygame.mouse.get_pos()):
            drawAllDotsButtonRect = drawAButton(DRAW_ALL_DOTS_BUTTON_TEXT, DRAW_ALL_DOTS_BUTTON_CENTER,WHITE,LIGHT_GREY)
        else:
            drawAllDotsButtonRect = drawAButton(DRAW_ALL_DOTS_BUTTON_TEXT, DRAW_ALL_DOTS_BUTTON_CENTER,WHITE,GREY)

        if drawCurrentDotButtonRect.collidepoint(pygame.mouse.get_pos()):
            drawCurrentDotButtonRect = drawAButton(DRAW_CURRENT_DOT_BUTTON_TEXT,DRAW_CURRENT_DOT_BUTTON_CENTER,WHITE,LIGHT_GREY)
        else:
            drawCurrentDotButtonRect = drawAButton(DRAW_CURRENT_DOT_BUTTON_TEXT,DRAW_CURRENT_DOT_BUTTON_CENTER,WHITE,GREY)

    #render the pi estimation screen
    elif menu == 1:
        #set the caption
        caption = pygame.display.set_caption(CAPTION_TEXT)

        #draw background circle
        backgroundCircle = pygame.draw.circle(screen, GREY, [WIDTH/2, HEIGHT/2], RADIUS)

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
            circleDots += 1
            dotColor = GREEN
        #increase the total number of circles 
        totalDots += 1

        #dot info for drawing the dot
        dotPosition = [x,y]
        
        if drawAllDots:
            #dot info for the current dot
            dotInfo = [dotPosition,dotColor]
            #add dot position and color to a list of dots to draw them
            dotInfoList.append(dotInfo)
            #draw current and previous dots
            for dotInfo in dotInfoList:
                #draw a dot with the color and position of the currently indexed dot info
                dotColor = dotInfo[1]
                dotPosition = dotInfo[0]
                pygame.draw.circle(screen,dotColor,dotPosition,2)
        else:
            #only draw the current dot
            pygame.draw.circle(screen,dotColor,dotPosition,2)

            
        #calculate pi
        result = 4 * (circleDots/totalDots)
        
        #draw back button
        backButtonRect = drawAButton(BACK_BUTTON_TEXT,BACK_BUTTON_CENTER,WHITE,GREY)

        #change the color of back button if you mouse over it
        if backButtonRect.collidepoint(pygame.mouse.get_pos()):
            backButtonRect = drawAButton(BACK_BUTTON_TEXT, BACK_BUTTON_CENTER,WHITE,LIGHT_GREY)
        else:
            backButtonRect = drawAButton(BACK_BUTTON_TEXT, BACK_BUTTON_CENTER,WHITE,GREY)

        #display the pi estimation
        text = FONT.render(str(result), True, WHITE)
        textRect = text.get_rect()
        textRect.bottomleft = (5,HEIGHT)
        screen.blit(text,textRect)


    for event in pygame.event.get():
        #if you click the x then quit
        if event.type == pygame.QUIT: sys.exit()
        #if you click a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            #draw all the dots and render the estimation
            if menu == 0 and drawAllDotsButtonRect.collidepoint(pygame.mouse.get_pos()):
                menu = 1
                drawAllDots = True
            #draw only the current dot and render the estimation
            elif menu == 0 and drawCurrentDotButtonRect.collidepoint(pygame.mouse.get_pos()):
                menu = 1
                drawAllDots = False
            #go back to the selection menu and resent values to defaults
            elif menu == 1 and backButtonRect.collidepoint(pygame.mouse.get_pos()):
                dotInfoList = []
                circleDots = 0
                totalDots = 0
                menu = 0

    pygame.display.update()