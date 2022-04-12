import pygame

# logo
icon = pygame.image.load("flappy-bird-assets/favicon.ico").convert()
pygame.display.set_icon(icon)


# couleurs
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,255)

# événements
NEW_PIPE = pygame.USEREVENT + 0
pygame.time.set_timer(NEW_PIPE,2000)


# images
base = pygame.image.load("flappy-bird-assets/sprites/base.png").convert()
background = pygame.image.load("flappy-bird-assets/sprites/background-day.png").convert()

# oiseaux
bird_bas = pygame.image.load("flappy-bird-assets/sprites/redbird-downflap.png").convert()
bird_millieu = pygame.image.load("flappy-bird-assets/sprites/redbird-midflap.png").convert()
bird_haut = pygame.image.load("flappy-bird-assets/sprites/redbird-upflap.png").convert()
birds = [bird_bas,bird_millieu,bird_haut]

# tuyaux
pipe_bas = pygame.image.load("flappy-bird-assets/sprites/pipe-red.png").convert()
pipe_haut = pygame.transform.flip(pipe_bas,True,True)

# score
score = 0
n0 = pygame.image.load("flappy-bird-assets/sprites/0.png")
n1 = pygame.image.load("flappy-bird-assets/sprites/1.png")
n2 = pygame.image.load("flappy-bird-assets/sprites/2.png")
n3 = pygame.image.load("flappy-bird-assets/sprites/3.png")
n4 = pygame.image.load("flappy-bird-assets/sprites/4.png")
n5 = pygame.image.load("flappy-bird-assets/sprites/5.png")
n6 = pygame.image.load("flappy-bird-assets/sprites/6.png")
n7 = pygame.image.load("flappy-bird-assets/sprites/7.png")
n8 = pygame.image.load("flappy-bird-assets/sprites/8.png")

# menu
menu = pygame.image.load("flappy-bird-assets/sprites/message.png")


# sons

saut = pygame.mixer.Sound("flappy-bird-assets/audio/swoosh.ogg")
saut.set_volume(0.1)

mort = pygame.mixer.Sound("flappy-bird-assets/audio/die.ogg")
mort.set_volume(0.3)

point = pygame.mixer.Sound("flappy-bird-assets/audio/point.ogg")
point.set_volume(0.05)
