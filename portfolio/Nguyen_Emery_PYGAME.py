
#This is a snake game GUI created by Cade Emery and Tran Nguyen.
#Created Using the tutorail of New Boston, although we put some touches on it.

#Import Statments------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import time
import random

#Start the Program------------------------------------------------------------------------------------------------------------------------------------------------------

pygame.init()

#Colors------------------------------------------------------------------------------------------------------------------------------------------------------

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (34, 177, 76)
blue = (0, 0, 155)
orange = (255, 140, 0)
light_green = (0,255, 0 )
light_orange= (244,179, 66 )
light_red = (239,113, 88 )


r = random.randint(0, 155)
g = random.randint(0, 155)
b = random.randint(0, 155)
randcolor = (r, g, b)

r1 = random.randint(155, 255)
g1 = random.randint(155, 255)
b1 = random.randint(155, 255)
randcolor2 = (r1,g1,b1)

#Screen Parameters------------------------------------------------------------------------------------------------------------------------------------------------------

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

#Variables------------------------------------------------------------------------------------------------------------------------------------------------------

clock = pygame.time.Clock()

block_size = 20  
FPS = 20

#Fonts------------------------------------------------------------------------------------------------------------------------------------------------------

smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Pause Section------------------------------------------------------------------------------------------------------------------------------------------------------

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Paused", black, -100, size="large")
        message_to_screen("Press C to continue or Q to quit", black, 25)
        pygame.display.update()
        clock.tick(5)

#Score Section------------------------------------------------------------------------------------------------------------------------------------------------------
        
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    
#Apple Placement Section------------------------------------------------------------------------------------------------------------------------------------------------------

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0

    return randAppleX, randAppleY

#Intro to the Game Section------------------------------------------------------------------------------------------------------------------------------------------------------

def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        gameDisplay.fill(white)
        message_to_screen("Welcome to SLITHER", green, -100, "large")
        message_to_screen("The objective of the game is to eat green apples", black, -30)
        message_to_screen("The more apples you eat, the longer you grow", black, 10)
        message_to_screen("If you run into yourself or the edges, you DIE 8)", black, 50)
        message_to_screen("Hint: Press P to pause in a game", black, 150)

        cur = pygame.mouse.get_pos()
        if 150+100> cur[0]>150 and 500+50>cur[1]>500:
            pygame.draw.rect(gameDisplay, light_green, (150, 500, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 500, 100, 50))

        if 350+100> cur[0]>350 and 500+50>cur[1]>500:
            pygame.draw.rect(gameDisplay, light_orange, (350, 500, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, orange, (350, 500, 100, 50))

        if 550+100> cur[0]>550 and 500+50>cur[1]>500:
            pygame.draw.rect(gameDisplay, light_red, (550, 500, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 500, 100, 50))
        

        button("Easy", 150, 500, 100 , 50, green, light_green, action = "Easy")
        button("Medium", 350, 500, 100 , 50, orange, light_orange, action = "Medium")
        button("Hard",  550, 500, 100 , 50, red, light_red, action = "Hard")
         

        pygame.display.update()
        clock.tick(15)

#Snake Characteristics------------------------------------------------------------------------------------------------------------------------------------------------------       

def snake(block_size, snakeList):
    
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, randcolor, [XnY[0], XnY[1],block_size,block_size])

#How Text Pops up on Screen------------------------------------------------------------------------------------------------------------------------------------------------------

def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), (buttony + (buttonheight / 2)))
    gameDisplay.blit(textSurf, textRect)

#How Buttons Appear------------------------------------------------------------------------------------------------------------------------------------------------------
                                          
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay,active_color,(x, y, width, height))
        if click[0] == 1 and action != None:
            #print("BUTTON PRESSED")
        
            if action == "Easy":
                gameLoop1()
            if action == "Medium":
                gameLoop2()
            if action == "Hard":
                gameLoop3()
            
            
        else:
            pygame.draw.rect(gameDisplay, inactive_color,(x, y, width, height))
            
        text_to_button(text, black, x, y, width, height)

#How Messages Appear------------------------------------------------------------------------------------------------------------------------------------------------------                                        

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace                             
    gameDisplay.blit(textSurf, textRect)

#Easy Game Mode------------------------------------------------------------------------------------------------------------------------------------------------------

def gameLoop1():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace = -50, size = "large")
            message_to_screen ("Press C to play again or Q to quit", black,50, size = "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop1()

        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size/2
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size/2
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size/2
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size/2
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
                         
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, AppleThickness, AppleThickness])

       
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)

        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print("x crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                
            
            
        
        
        clock.tick(FPS)
    pygame.quit()
    quit()

#Medium Gamemode------------------------------------------------------------------------------------------------------------------------------------------------------
    
def gameLoop2():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace = -50, size = "large")
            message_to_screen ("Press C to play again or Q to quit", black,50, size = "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop2()

        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
                         
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, AppleThickness, AppleThickness])

       
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)

        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print("x crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                
            
            
        
        
        clock.tick(FPS)
    pygame.quit()
    quit()

#Hard Gamemode------------------------------------------------------------------------------------------------------------------------------------------------------

def gameLoop3():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace = -50, size = "large")
            message_to_screen ("Press C to play again or Q to quit", black,50, size = "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop3()

        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size*2
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size*2
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size*2
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size*2
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
                         
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, AppleThickness, AppleThickness])

       
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)

        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print("x crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                
                randAppleX,randAppleY = randAppleGen()
                snakeLength +=1
                
            
            
#Variable Calling------------------------------------------------------------------------------------------------------------------------------------------------------       
        
        clock.tick(FPS)
    pygame.quit()
    quit()

    
game_intro()
gameLoop1()
gameLoop2()
gameLoop3()


