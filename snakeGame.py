"""
Hey Everyone!
This is a simple Snake Game developed using pygame with python 3
"""
__author__ = "Darshan Majithiya"
__email__ = "darsh2115@gmail.com"
__version__ = "1.1"

# Game imports
import pygame, sys, random, time

# Check for initializing errors
check_errors = pygame.init()
if(check_errors[1]):
    print("! Had {0} initializing erros, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initalized!")

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game') # setting window title

# Colors
red = pygame.Color(255, 0, 0) # Game Over Message
green = pygame.Color(0, 255, 0) # Snake 
black = pygame.Color(0, 0, 0) # Score
white = pygame.Color(255, 255, 255) # Background
brown = pygame.Color(165, 42, 42) # Food

# FPS Controller
fpsCOntroller = pygame.time.Clock()

# Important Variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
score = 0

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

# Direction
direction = 'RIGHT'
changeto = direction

# Game over Function
def gameOver():
    '''The gameOver() display the Message and the score to the user.'''
    myFont = pygame.font.SysFont('monaco', 72)
    GOSurface = myFont.render('Game Over :(', True, red)
    GOrect = GOSurface.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOSurface, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() # pygame exit
    sys.exit() # console exit
 
# Show Score Function
def showScore(choice = 1):
    scoreFont = pygame.font.SysFont('monaco', 32)
    scoreSurface = scoreFont.render('Score: {0}'.format(score), True, black)
    scorerect = scoreSurface.get_rect()
    if(choice):
        scorerect.midtop = (80, 10)
    else:
        scorerect.midtop = (360, 85)
    playSurface.blit(scoreSurface, scorerect)

# Main Logic of the game
while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT or event.key == ord('d')):
                changeto = 'RIGHT'
            if(event.key == pygame.K_LEFT or event.key == ord('a')):
                changeto = 'LEFT'
            if(event.key == pygame.K_UP or event.key == ord('w')):
                changeto = 'UP'
            if(event.key == pygame.K_DOWN or event.key == ord('s')):
                changeto = 'DOWN'
            if(event.key == pygame.K_ESCAPE):
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of Direction
    if(changeto == 'RIGHT' and not direction == 'LEFT'):
        direction = 'RIGHT'
    if(changeto == 'LEFT' and not direction == 'RIGHT'):
        direction = 'LEFT'
    if(changeto == 'UP' and not direction == 'DOWN'):
        direction = 'UP'
    if(changeto == 'DOWN' and not direction == 'UP'):
        direction = 'DOWN'

    # Updating the Coordinates of snake
    if(direction == 'RIGHT'):
        snakePos[0] += 10
    if(direction == 'LEFT'):
        snakePos[0] -= 10
    if(direction == 'UP'):
        snakePos[1] -= 10
    if(direction == 'DOWN'):
        snakePos[1] += 10

    #Body Mechanism
    snakeBody.insert(0, list(snakePos))
    if(snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]):
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    # Food Spawn
    if(foodSpawn == False):
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True

    playSurface.fill((255, 255, 255)) # setting the surface color to white

    # Drawing the Snake Body
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    #Drawing the Food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))   
    
    # Boundary Constraint
    if(snakePos[0] > 710 or snakePos[0] < 0):
        gameOver()
    if(snakePos[1] > 450 or snakePos[1] < 0):
        gameOver()

    # Self Hit
    for block in snakeBody[1:]:
        if(snakePos[0] == block[0] and snakePos[1] == block[1]):
            gameOver()

    # Common Mechanism
    showScore()
    pygame.display.flip()
    fpsCOntroller.tick(8)
