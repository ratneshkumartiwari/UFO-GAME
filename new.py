import pygame
import random
import math

# initiaising pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#background iamge
background = pygame.image.load('back.png ')

#player
playerImg = pygame.image.load('spaceship (1).png')
playerX = 350
playerY = 480
playerX_change = 0

#invaders
invadersImg = []
invaderX = []
invaderY = []
invaderX_change = []
invaderY_change = []
number_of_enimies = 4
for i in range(number_of_enimies):
    invadersImg.append(pygame.image.load('alien.png'))
    invaderX.append(random.randint(0,736))
    invaderY.append(random.randint(50,100))
    invaderX_change.append(2)
    invaderY_change.append(40)

#collision
distance = 0
score = 0

#bullets
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg, (x,y))


def invaders(x,y, i):
    screen.blit(invadersImg[i], (x,y))

def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))

def isCollision(invaderX, invaderY, bulletX, bulletY):
    distance = math.sqrt(math.pow(invaderX - bulletX, 2) + math.pow(invaderY - bulletY, 2))
    if distance <= 16:
        return True
    else:
        False



# game loop
running = True
while running:
    # RGB = RED, GREEN, BLUE
    screen.fill((0, 128, 176))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # gets the current x coordinate of player
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(number_of_enimies):
        invaderX[i] += invaderX_change[i]


        if invaderX[i] <= 0:
            invaderX_change[i] = 4
            invaderY[i] += invaderY_change[i]

        if invaderX[i] >= 736:
            invaderX_change[i] = -4
            invaderY[i] += invaderY_change[i]

        collision = isCollision(invaderX[i], invaderY[i], bulletX, bulletY)
        if collision == True:
            bulletY = 480
            bullet_state = "ready"
            invaderX[i] = random.randint(0, 736)
            invaderY[i] = random.randint(50, 100)
            score += 1
            print(score)

        invaders(invaderX[i], invaderY[i], i)

    if bullet_state is "fire":
        bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    if bulletY == 0:
        bullet_state = "ready"
        bulletY = 480






    player(playerX,playerY)

    pygame.display.update()



