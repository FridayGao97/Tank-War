# https://pythonprogramming.net/pygame-python-3-part-1-intro/
import pygame
import time
import random
import os
import wall
import Player

pygame.init()
pygame.mixer.init()

display_width = 1064
display_height = 864

#set the size of display windows
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set the title to print on the top of windows
pygame.display.set_caption('Tank War')

# defining colors, using RGB formatting
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)
orange = (255,69,0)
white = (255, 255, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)

#this is a our game clock. We use this to track time within the game, and this is mostly used for FPS, or "frames per second."
clock = pygame.time.Clock()
# the car does not crash a rock

#load the car
carImg = pygame.image.load('racecar.png')
car_size = [73,73]
pause = False
Player = 1




#function for building (drawing) a car
def car(x,y):
    #"Blit" basically just draws the image to the screen, but we still have yet to fully show it to the display. 
    # In graphics, generally, there is a lot done in the background, 
    #and only when every update is done is when the screen is visually updated.
    gameDisplay.blit(carImg, (x,y))


#takes x, y starting points, width and height variables, and finally a color.
# creat block
def thingsHappen(thingx, thingy, thingw, thingh, color):
    #pygame.draw.rect() to draw the polygon to our specifications. 
    #The parameters to this function are : where, what color, and then the x,y location followed by the width and the height.
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#text for crash
def text_object(text,font,color = black):
    textSurface = font.render(text, True , color)
    #using .get_rect() to get the rectangle that is somewhat invisible, so we can reference it and center the text.
    return textSurface, textSurface.get_rect()
def print_message(text):
    #define the large text
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #define the text and the rectangle that would encompass largetext
    TextSurf, TextRect = text_object(text, largeText,red)
    #center the text, using our width and height variables (the gift that keeps on giving
    TextRect.center = ((display_width/2),(display_height/2))

    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
           action()
                     
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        IntroImg = pygame.image.load(os.path.join('Image','gameIntro.png'))
        gameDisplay.blit(IntroImg, (300,250))       
        # gameDisplay.fill(black)
        # largeText = pygame.font.Font('freesansbold.ttf',115)


        button("1 Player",220,450,100,50,green,bright_green,main1)
        button("2 Players",420,450,100,50,green,bright_green,main2)
        button("Quit",620,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        #15 frames per second
        clock.tick(15)

def main1():
    global Player
    Player = 1
    main()
def main2():
    global Player
    player = 2
    main()

def Paused():
    global pause
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_object("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause :

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     
                    unpaused()
                    break
            

              
        #gameDisplay.fill(white)

        button("Continue",150,450,100,50,green,bright_green,unpaused)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        

        pygame.display.update()
        clock.tick(15)
    
    

#crashed
def GameOver():
    gameDisplay.fill(black)
    OverImg = pygame.image.load(os.path.join('Image','gameover.png'))
    gameDisplay.blit(OverImg, (400,350))
    
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    game_intro()

def unpaused():
    global pause
    pause = False

#print the score at the left top of screen
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def main():
    gameDisplay.fill(black)
    global Player

    #load sound
    bang_sound = pygame.mixer.Sound(os.path.join('sound',"bang.wav"))
    bang_sound.set_volume(1)
    fire_sound = pygame.mixer.Sound(os.path.join('sound',"Gunfire.wav"))
    start_sound = pygame.mixer.Sound(os.path.join('sound',"start.wav"))
    start_sound.play()

    # 定义精灵组:坦克，我方坦克，敌方坦克，敌方子弹
    allTankGroup     = pygame.sprite.Group()
    mytankGroup      = pygame.sprite.Group()
    allEnemyGroup    = pygame.sprite.Group()
    redEnemyGroup    = pygame.sprite.Group()
    greenEnemyGroup  = pygame.sprite.Group()
    otherEnemyGroup  = pygame.sprite.Group()  
    enemyBulletGroup = pygame.sprite.Group()

    # initial the Map of Wall 
    bgMap = wall.Map()


    #initial user's tank or tanks
    if Player == 1:
	    myTank_T1 = myTank.MyTank(1)
        allTankGroup.add(myTank_T1)
        mytankGroup.add(myTank_T1)
    elif: Player ==2:
    	myTank_T1 = myTank.MyTank(1)
        allTankGroup.add(myTank_T1)
        mytankGroup.add(myTank_T1)

	    myTank_T2 = myTank.MyTank(2)
        allTankGroup.add(myTank_T2)
        mytankGroup.add(myTank_T2)


    # inital enemies' tank
    for i in range(1, 4):
            enemy = enemyTank.EnemyTank(i)
            allTankGroup.add(enemy)
            allEnemyGroup.add(enemy)
            if enemy.isred == True:
                redEnemyGroup.add(enemy)
                continue
            if enemy.kind == 3:
                greenEnemyGroup.add(enemy)
                continue
            otherEnemyGroup.add(enemy)
    # 敌军坦克出现动画
    appearance_image = pygame.image.load(os.path.join('Image','appear.png'))
    
    appearance = []
    appearance.append(appearance_image.subsurface(( 0, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((48, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((96, 0), (48, 48)))

    # 自定义事件
    # 创建敌方坦克延迟500
    DELAYEVENT = pygame.constants.USEREVENT
    pygame.time.set_timer(DELAYEVENT, 200)
    # 创建 敌方 子弹延迟1000
    ENEMYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 1
    pygame.time.set_timer(ENEMYBULLETNOTCOOLINGEVENT, 1000)
    # 创建 我方 子弹延迟200
    MYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 2
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT, 200)
    # 敌方坦克 静止8000
    NOTMOVEEVENT = pygame.constants.USEREVENT + 3
    pygame.time.set_timer(NOTMOVEEVENT, 8000)
    
    
    delay = 100
    moving = 0
    movdir = 0
    moving2 = 0
    movdir2 = 0
    enemyNumber = 3
    enemyCouldMove      = True
    switch_R1_R2_image  = True
    homeSurvive         = True
    running_T1          = True
    running_T2          = True
    clock = pygame.time.Clock()
    while True:












    #starting points for car
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    car_speed = 1
    dodged = 0
    

    #the initial location of block, its width and height
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    crashed = False
    

    while crashed is False:
        #   Here, we've filled our display with a color, white. What this does is cover everything in white.
        #   Paint the game white, so-to-speak. This will cover over any existing stuff. 
        #   After that, we run our car function to draw the car to the screen. 
        gameDisplay.fill(black) #background
        # things(thingx, thingy, thingw, thingh, color)
        thingsHappen(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_starty += thing_speed

        
        #to get the movement of car
        for event in pygame.event.get():
            #print(event)
            #if the user exit out of the window
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = +5
                if event.key == pygame.K_SPACE:
                    global pause
                    pause = True
                    Paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            
        #update the car location
        x += x_change * car_speed 
        y += y_change * car_speed

        #restriction for x,y coordinate
        if x > display_width - car_size[0]:
            x = display_width - car_size[0]  
        elif x < 0:
            x = 0  
        if y > display_height - car_size[1]:
            y = display_height - car_size[1]
        elif y < 0:
            y = 0

        #draw the car new location
        car(x,y)

        if x >= thing_startx and x <= thing_startx + thing_width:
            if y <= thing_starty and y >= thing_starty - thing_height:
                GameOver()

                

        # if bolck pass to down, go top again
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            #add count score
            dodged += 1
            #increase difficulity
            thing_speed += 0.5
            thing_width += (dodged * 1.2)

        
        #update the score
        things_dodged(dodged)
        pygame.display.update()
        #Basically, this is how many frames per second we are running. In this case, we are running 60 FPS.
        # we can increase the FPS to speed up
        clock.tick(60)
    quitgame()


def quitgame():
    pygame.quit()
    quit()

game_intro()
main()
quitgame()
