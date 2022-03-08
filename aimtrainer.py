import pygame
from pygame.locals import *
import sys
import random
pygame.init()


size = [40,40] # size of Dots
win_size = 100 #window size
win_ratio = [16,9] #window ratio
colort = (200,150,200) #color of the text
colorb = (200,0,0) #color of target
verbose = 0 #verbose mode
countdown = 60 #time to score


tar_num = 3 
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
start_ticks=pygame.time.get_ticks() #starter tick


counter, text = 10, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

score = 1
missed = 0
accuracy = 0
click = 0
click2 = 0
click3 = 0

display = pygame.display.set_mode((win_size * win_ratio[0], win_size * win_ratio[1]))
FPS_CLOCK = pygame.time.Clock()

pos = [100,100]
tar_pos=[[0 for i in range(2)] for j in range(tar_num)]

def writeText(string, coordx, coordy, fontSize):
    #set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, colort)
    #get the rect of the text
    textRect = text.get_rect()
    #set the position of the text
    textRect.center = (coordx, coordy)
    #add text to window
    display.blit(text, textRect)

c = 0
i=0
while i <= tar_num-1:
    tar_pos[i][0]=random.randint(0,win_size*win_ratio[0]-50)
    tar_pos[i][1]=random.randint(0,win_size*win_ratio[1]-50)
    i+=1

i=0
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        global c
        self.rect = pygame.draw.rect(display, colorb, (tar_pos[c][0], tar_pos[c][1],  size[0],size[1]))
        c += 1
        if verbose == 1:
            print("init")
    def update(self):
        self.rect = pygame.draw.rect(display, colorb, (tar_pos[0][0], tar_pos[0][1],  size[0],size[1]))

    def update2(self):
        self.rect = pygame.draw.rect(display, colorb, (tar_pos[1][0], tar_pos[1][1],  size[0],size[1]))
    def update3(self):
        self.rect = pygame.draw.rect(display, colorb, (tar_pos[2][0], tar_pos[2][1],  size[0],size[1]))
player = Player()
player2 = Player()
player3 = Player()



    


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if event.type == pygame.USEREVENT: 
            counter += 1


        if event.type == pygame.MOUSEBUTTONDOWN:    
            if player2.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse clicked on the Player2")
                click2 = 1

            if player.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse clicked on the Player")
                click = 1

            if player3.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse clicked on the Player3")
                click3 = 1

            if click == 0 and click2 == 0 and click3 == 0:
                missed += 1
                if verbose == 1:
                    print("missed")
              
        if event.type == pygame.MOUSEBUTTONUP:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse released on the Player")
                if click == 1:
                    tar_pos[0][0]=random.randint(0,win_size*win_ratio[0]-50)
                    tar_pos[0][1]=random.randint(0,win_size*win_ratio[1]-50)
                    if verbose == 1:
                        print(tar_pos)
                    score += 1
                    click = 0
            if player2.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse released on the Player2")
                if click2 == 1:
                    tar_pos[1][0]=random.randint(0,win_size*win_ratio[0]-50)
                    tar_pos[1][1]=random.randint(0,win_size*win_ratio[1]-50)
                    score += 1
                    click2 = 0
                    print(tar_pos)

            if player3.rect.collidepoint(pygame.mouse.get_pos()):
                if verbose == 1:
                    print("Mouse released on the Player3")
                if click3 == 1:
                    tar_pos[2][0]=random.randint(0,win_size*win_ratio[0]-50)
                    tar_pos[2][1]=random.randint(0,win_size*win_ratio[1]-50)
                    #tar_pos[i][1]=0,win_size*win_ratio[0]-50,random.randint(0,win_size*win_ratio[1]-50)

                    pos = [random.randint(0,win_size*win_ratio[0]-50),random.randint(0,win_size*win_ratio[1]-50)]
                    score += 1
                    click3 = 0
                    print(tar_pos)





    if (countdown-seconds) <= 0:
        display.fill(BLACK)
        writeText("Accuracy: " + str(100-int(accuracy)),(win_size*win_ratio[0])/2,(win_size*win_ratio[1])/2-100,100)
        writeText("Shots: " + str(score),(win_size*win_ratio[0])/2,(win_size*win_ratio[1])/2,100)
        pygame.display.update()
    else:
        accuracy = (100/(score+missed))*missed
        display.fill(BLACK)
        display.blit(font.render(str(int(countdown-seconds)), True, colort), (win_size*16-130, 0))
        #player.draw(display)
        writeText(str(score),100,100,100)
        #accuracy = 
        writeText(str(100-(int(accuracy))),600,100,100)
        player.update()
        player2.update2()
        player3.update3()
        pygame.display.update()
        FPS_CLOCK.tick(60)