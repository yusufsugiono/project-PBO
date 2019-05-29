import pygame, sys
import random
from pygame.locals import *

#Audio Setting
pygame.mixer.pre_init(44100, 16, 2, 4096)

#Declare globals and initiate pygame
pygame.init()
WHITE= (255,255,255)
PINK = (145, 98, 110)
BLACK = (0,0,0)
BLUE = (255)
HEIGHT = 400
WIDTH = 700
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PINGPONG')
CLOCK = pygame.time.Clock()
FPS = 60

#Playing Backsound
pygame.mixer.music.load('audio/1.wav')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

font_name = pygame.font.match_font('arial')


class Paddle(pygame.sprite.Sprite):
    def __init__(self, centery, centerx, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 60))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedy = 0
        self.player = player

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #Paddle movement
        if self.player == 2:
            if keystate[pygame.K_UP]:
                self.speedy -= 7
            elif keystate[pygame.K_DOWN]:
                self.speedy += 7
            self.rect.y += self.speedy
        elif self.player == 1:
            if ball.speedx < 0:
                if ball.rect.centery == self.rect.centery:
                    self.speedy = 0
                elif ball.rect.centery > self.rect.centery:
                    self.speedy += 4
                elif ball.rect.centery < self.rect.centery:
                    self.speedy -= 4
            elif ball.speedx > 0:
                if self.rect.centery == HEIGHT/2:
                    self.speedy += 0
                elif self.rect.centery < HEIGHT/2:
                    self.speedy += 4
                elif self.rect.centery > HEIGHT/2:
                    self.speedy -= 4
            #Comment out above and use this instead if you want to play against another player.
            #if keystate[pygame.K_w]:
            #    self.speedy -= 5
            #if keystate[pygame.K_s]:
            #    self.speedy += 5
            self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.ballspeed = 3
        self.speedx = random.choice([7, -7])
        self.speedy = 3
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        self.scoreplayer1 = 0
        self.scoreplayer2 = 0
        self.nyawaplayer1 = 3
        self.nyawaplayer2 = 3


    def update(self):
        self.speedy = self.speedy
        self.speedx = self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy
        elif self.rect.bottom > HEIGHT:
            self.speedy = -self.speedy
        if pygame.sprite.collide_rect(self, paddle):
            self.speedx = -(self.speedx)
            #self.speedx += .5
        elif pygame.sprite.collide_rect(self, paddle2):
            self.speedx = -(self.speedx)
            #self.speedx -= .5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = random.choice([2, -2])
            self.scoreplayer2 += 1
            self.nyawaplayer1 -= 1

        elif self.rect.left < 0:
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = random.choice([2, -2])
            self.scoreplayer1 += 1
            self.nyawaplayer2 -= 1

if __name__ == '__main__':
    #Create sprites group and add both our paddles and the ball
    all_sprites = pygame.sprite.Group()
    paddle = Paddle(HEIGHT/2, 10, 1)
    paddle2 = Paddle(HEIGHT/2, WIDTH - 10, 2)
    ball = Ball()
    all_sprites.add(paddle)
    all_sprites.add(paddle2)
    all_sprites.add(ball)
    

    #Game Loop

    running = True
    while running:

        # keep loop running at the right speed
        CLOCK.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
        #Update sprites
        all_sprites.update()
        #Draw everything to the screen
        #Fill blank background
        DISPLAY.fill(BLACK)

        #fill background with photos
        #DISPLAY.blit(bg,(0,0))
        all_sprites.draw(DISPLAY)
        Paddle.draw_text(DISPLAY, ("Score: "+str(ball.scoreplayer2)), 18, 50, 10)
        Paddle.draw_text(DISPLAY, ("Life : "+str(ball.nyawaplayer2)), 18, 50, 30)
        Paddle.draw_text(DISPLAY, ("Score: "+str(ball.scoreplayer1)), 18, 650, 10)
        Paddle.draw_text(DISPLAY, ("Life : "+str(ball.nyawaplayer1)), 18, 650, 30)
        pygame.display.flip()
        CLOCK.tick(FPS)
        

    pygame.quit()
    quit()
