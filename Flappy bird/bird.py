#导入轮子
import pygame
from random import randrange
from time import sleep
pygame.init()

frame=0
map_width=284
map_height=512
FPS=60
pipes = [[180,4]]
bird=[40,map_height//2-50]
gravity = 0.2
velocity = 0

gameScreen = pygame.display.set_mode((map_width,map_height))
clock=pygame.time.Clock()

bird_wing_up = bird_wing_up_copy = pygame.image.load('images/bird_wing_up.png')
bird_wing_down = bird_wing_down_copy = pygame.image.load('images/bird_wing_down.png')
background = pygame.image.load('images/background.png')
pipe_body = pygame.image.load('images/pipe_body.png')
pipe_end = pygame.image.load('images/pipe_end.png')

def draw_pipes():
    global pipes
    
    for i in range(len(pipes)):
        
        for n in range(pipes[i][1]):
            gameScreen.blit(pipe_body , (pipes[i][0] , n*32))
        
        for n in range(pipes[i][1]+6 , 16):
            gameScreen.blit(pipe_body , (pipes[i][0] , n*32))
        
        gameScreen.blit(pipe_end , (pipes[i][0] , (pipes[i][1])*32))
        gameScreen.blit(pipe_end , (pipes[i][0], (pipes[i][1]+5)*32))
        pipes[i][0] -= 1

def draw_bird(x,y):
    global frame
    
    if 0<=frame<=30:
        gameScreen.blit(bird_wing_up,(x,y))
        frame += 1
    elif 30<frame<=60:
        gameScreen.blit(bird_wing_down,(x,y))
        frame += 1
        if frame==60 : frame=0

def safe():
    
    if bird[1]>map_height-35:
        print('hit floor')
        return False
    
    if bird[1]<0:
        print('hit ceiling')
        return False
    
    if pipes[0][0]-30 < bird[0]  < pipes[0][0]+79:
        
        if bird[1]<(pipes[0][1]+1)*32 or bird[1]>(pipes[0][1]+4)*32:
            print('hit pipe')
            return False
    
    return True

def reset():
    global frame,map_width,map_height,FPS,pipes,bird,gravity,velocity

    frame=0
    map_width=284
    map_height=512
    FPS=60
    pipes.clear()
    bird.clear()
    pipes=[[180,4]]
    bird=[40,map_height//2-50]
    gravity = 0.2
    velocity = 0

#游戏主循环
def gameLoop():
    global velocity

    while True:
        
        if len(pipes)<4:
            x=pipes[-1][0]+200
            open_pos=randrange(1,9)
            pipes.append([x,open_pos])
        if pipes[0][0]<-80:
            pipes.pop(0)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                bird[1] -= 40
                velocity = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        #物理引擎
        velocity += gravity
        bird[1] += velocity
        #不知道为什么，这个旋转实现不了，先写着里吧，找到原因了再说
        bird_wing_down = pygame.transform.rotate(bird_wing_down_copy, 90*(velocity//15))
        bird_wing_up = pygame.transform.rotate(bird_wing_up_copy, 90*(velocity//15))
        
        
        gameScreen.blit(background,(0,0))
        draw_pipes()
        draw_bird(bird[0],bird[1])
        pygame.display.update()
        
        if not safe():
            sleep(3)
            reset()
        clock.tick(FPS)


gameLoop()
