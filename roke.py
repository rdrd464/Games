import pygame
import random
from pygame import mixer
import math
# # initialize the pygame
pygame.init()
# create screen
screen=pygame.display.set_mode((800,600))
# Title and Icon logo
pygame.display.set_caption("Rock Game")
icon=pygame.image.load('tank.png')
pygame.display.set_icon(icon)
#Background Image
background=pygame.image.load('desert.png')
# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)
#Tank
tank=pygame.image.load('tank (1).png')
tankX=370
tankY=480
tankX_change=0
# Rock

rocks=[]
rockX=[]
rockY=[]
rockX_change=[]
rockY_change=[]
nu_of_rocks=15
for n in range(nu_of_rocks):
    rocks.append(pygame.image.load('rock.png'))
    rockX.append(random.randint(0, 735))
    rockY.append(random.randint(50, 150))
    rockX_change.append(0.4)
    rockY_change.append(40)
# sorce font
value=0
font=pygame.font.Font('freesansbold.ttf',30)
textXX=10
textYY=10

# fire
fire1=pygame.image.load('bullet.png')
fireX=0
fireX_change=0
fireY=480
fireY_change=10
fire_state="ready"
# Game overr
over_font=pygame.font.Font('freesansbold.ttf',60)
def firee(x,y):
    global fire_state
    fire_state="fire"
    screen.blit(fire1,(x+16 ,y +10))
def game_over():
    over=over_font.render("Over Game !!",True,(115,55,25))
    screen.blit(over,(200,250))
def rock(x,y,n):
    screen.blit(rocks[n],(x,y))
def tank_g(x,y):
  screen.blit(tank,(x,y))
def coll(tankX,tankY,fireX,fireY):
    distance=math.sqrt((math.pow(tankX-fireX,2))+(math.pow(tankY-fireY,2)))
    if distance<27:
        return True
    else:
        return False
def show_s(x,y):
    s=font.render("The sorce : "+str(value),True,(255,255,255))
    screen.blit(s,(x,y))
run=True
while run:
    screen.fill((204,102,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
      if event.type== pygame.QUIT:
          run=False
      if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_LEFT:
              tankX_change= -0.5
          if event.key == pygame.K_RIGHT:
              tankX_change =0.5
          if event.key == pygame.K_SPACE:
              if fire_state=="ready":
                  soundc=mixer.Sound('bumb.mp3')
                  soundc.play()
                  fireX=tankX
                  firee(fireX,fireY)
      if event.type==pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              tankX_change=0
  # Bounderies Check
    tankX += tankX_change
    if tankX<=0:
        tankX=0
    elif tankX>=736:
        tankX=736
    # Rock Movement
    for n in range(nu_of_rocks):
       if rockY[n]>200:
            for m in range(nu_of_rocks):
                rockY[m]=2000
            game_over()
            break
       rockX[n] += rockX_change[n]
       if rockX[n] <= 0:
         rockX_change[n] = 0.5
         rockY[n] += rockY_change[n]
       elif rockX[n] >= 736:
           rockX_change[n] = -0.5
           rockY[n] += rockY_change[n]
      # Collision
       col=coll(rockX[n],rockY[n],fireX,fireY)
       if col:
         Soi=mixer.Sound('New_Super.mp3')
         Soi.play()
         fireY=480
         fire_state="ready"
         value += 1
         rockX[n]=random.randint(0,735)
         rockY[n]=random.randint(50,150)
       rock(rockX[n],rockY[n],n )

   # Fire Movement
       if fireY<=0:
          fireY=480
          fire_state="ready"
       if fire_state == "fire":
           firee(fireX,fireY)
           fireY -= fireY_change

    tank_g(tankX,tankY)
    show_s(textXX,textYY)
    pygame.display.update()
