import random
import pygame 
from pygame.locals import *
import os


pygame.init()
largeur = 288
hauteur = 512
screen = pygame.display.set_mode((largeur,hauteur))
os.chdir(__file__[:-8])
from variables import *
pygame.display.set_caption("Flappy Bird")
# pygame.mouse.set_visible(False)
clock = pygame.time.Clock()



n9 = pygame.image.load("flappy-bird-assets/sprites/9.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_bas
        self.images = birds
        self.image_bas = self.images[0]
        self.image_millieu = self.images[1]
        self.image_haut = self.images[2]

        self.rect = self.images[0].get_rect()
        self.rect.x = 5
        self.velocity = 0

    def update(self):
        self.rect.y += self.velocity
        collisions = pygame.sprite.spritecollide(bird,tuyaux,True)
        if collisions or self.rect.y > hauteur - 125 or self.rect.y < 0:
            mort.play()
            pygame.time.delay(1000)
            pygame.quit()


class Tuyau(pygame.sprite.Sprite):
    def __init__(self,direction,y):
        super().__init__()
        if direction == "haut":
            self.image = pipe_haut
            # self.y = -random.randint(0,200)
            self.y = -285 + y
        if direction == "bas":
            self.image = pipe_bas
            self.y = 130 + y 

        self.rect = self.image.get_rect()
        self.rect.x = largeur - self.rect.width
        self.rect.x = largeur 
        self.rect.y = self.y
    
    def update(self):
        self.rect.x -= 2
        if self.rect.x < -self.rect.width:
            global score
            score += 0.5
            self.kill()
            if int(score) == score : # si le score est un entier
                point.play()

def transform_number(n):
    """
    transforme un nombre en image avec une surface transparente a laquelle on colle les images des chiffres
    """
    # surface transparente vide
    surface = pygame.Surface((60,50),pygame.SRCALPHA)
    p = 0
    for i in str(int(n)): # parcours chaque chiffre du nombre
        if i == "0":
            surface.blit(n0,(p,0))
            p += 20
        if i == "1":
            surface.blit(n1,(p,0))
            p += 20
        if i == "2":
            surface.blit(n2,(p,0))
            p += 20
        if i == "3":
            surface.blit(n3,(p,0))
            p += 20
        if i == "4":
            surface.blit(n4,(p,0))
            p += 20
        if i == "5":
            surface.blit(n5,(p,0))
            p += 20
        if i == "6":
            surface.blit(n6,(p,0))
            p += 20
        if i == "7":
            surface.blit(n7,(p,0))
            p += 20
        if i == "8":
            surface.blit(n8,(p,0))
            p += 20
        if i == "9":
            surface.blit(n9,(p,0))
            p += 20
    return surface



bird = Bird()
bird.rect.y = hauteur/2
tuyaux = pygame.sprite.Group()

on_menu = True

finished = False
while not finished :
    clock.tick(60)

    ##### EVENTS #####
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN :
            saut.play()
            if on_menu:
                on_menu = False
                bird.velocity = -8
            if bird.velocity -9 > -9:
                bird.velocity -= 9
            else:
                bird.velocity = -6

        if event.type == NEW_PIPE:
            if not on_menu :
                y = random.randint(0,200)
                tuyaux.add(Tuyau("haut",y))
                tuyaux.add(Tuyau("bas",y))

        if event.type == pygame.QUIT:
            finished = True

    ##### DRAW #####
    screen.fill(BLACK)

    screen.blit(background,(0,0))
   

    if bird.velocity <= 2 and not on_menu: # pour ne pas tomber trop vite
        bird.velocity += 0.5


    if bird.velocity <= -1:
        bird.image = bird_haut
    elif bird.velocity >= 1:
        bird.image = bird_bas
    else:
        bird.image = bird_millieu

    bird.update()
    screen.blit(bird.image,bird.rect)
    
    tuyaux.update()
    tuyaux.draw(screen)
    image = transform_number(score)
    screen.blit(image,(largeur//2 - image.get_size()[0]//2 ,35)) # centre le score en haut 
    screen.blit(base,(0,hauteur - base.get_height()))
    if on_menu:
        screen.blit(menu,(largeur//2 - menu.get_size()[0]//2,hauteur//2 - menu.get_size()[1]//2))

    pygame.display.flip()

