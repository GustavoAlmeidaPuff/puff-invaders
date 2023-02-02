import pygame
import random

pygame.init()


x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('meu jogo feito com python')


bg = pygame.image.load ('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(x,y))


alien = pygame.image.load('images/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alien, (90,90))


playerimg = pygame.image.load('images/space.png').convert_alpha()
playerimg = pygame.transform.scale(playerimg, (80,80))
playerimg = pygame.transform.rotate(playerimg, -90)

missil = pygame.image.load('images/missle.png').convert_alpha()
missil = pygame.transform.scale(missil, (50,50))


pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 210
pos_player_y = 310

vel_x_missil = 0 
pos_x_missil = 210
pos_y_missil = 310

pontos = 3

triggered = False

rodando = True

font = pygame.font.SysFont ('arial', 50)

player_rect = playerimg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

#função respawn
def respawn():
    x = 1350
    y = random.randint(1,640)
    return[x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_Y = pos_player_y
    vel_x_missil = 0
    return[respawn_missil_x, respawn_missil_Y, triggered, vel_x_missil]

def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False
    

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    screen.blit(bg,(0,0))
    
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect ().width,0))#cria background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    

    #teclas

    #UP
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 2
        if not triggered:
            pos_y_missil -=2

    #DOWN
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 2
        if not triggered:
            pos_y_missil +=2

    
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 5

    
    if pontos == 0:
        rodando = False


    #respawn

    if pos_alien_x == 10:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    if pos_x_missil == 1300:
        pos_x_missil,pos_y_missil, triggered, vel_x_missil = respawn_missil()

    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]


    #posiçoes rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y

    #movimento
    x -= 1


    ##################################
    #VELOCIDADE DOS ALIENS
    #mude aqui o nivel de dificuldade
    pos_alien_x -= 3
    ##################################

    
    pos_x_missil += vel_x_missil

    #prova real da colisão
    #pygame.draw.rect(screen, (255, 0, 0),player_rect, 4)
    #pygame.draw.rect(screen, (255, 0, 0),missil_rect, 4)
    #pygame.draw.rect(screen, (255, 0, 0),alien_rect, 4)

    score = font.render (f'pontos: {int(pontos)} ', True, (255,255,255))
    screen.blit(score,(50,50))

    #criar imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil,(pos_x_missil,pos_y_missil))
    screen.blit(playerimg, (pos_player_x, pos_player_y))

    pygame.display.update()