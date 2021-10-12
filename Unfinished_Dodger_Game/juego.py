# dodger autor Alex Martorell

import pygame
import math
import clases
import random
#-----------------------------------------------------
num_enemigos = 0
score = 0
enemigos = []
num_max_enemigos = 15
#el juego termina cuando se le acaban las vidas a dodgy
def gameover(dodgy):
    if dodgy.vidas==0:
        return True
    else: return False

#muestra la imagen de cualquier entidad
def mostrar_imagen(screen, entidad):
    screen.blit(entidad.im,(entidad.posx, entidad.posy))

#un enemigo muere y aumenta el score
def muerte_enemigo(enemigo):
    if enemigo.posy == 536 :
        enemigos.remove(enemigo)



#si chocas con un enemigo
def colision(enemigo, dodgy):
    if(math.sqrt(math.pow((dodgy.posx-enemigo.posx),2)+math.pow((dodgy.posy-enemigo.posy),2))<70 and not enemigo.colision):
        dodgy.posx = 350
        dodgy.posy = 470
        enemigo.colision = True
        return True
    return False

def spawn():
    while len(enemigos)<num_max_enemigos:
            enemigos.append(clases.enemy(random.randint(50,750),-50,"rojo.png"))


def main():
    gameover = False
    puntuacion = 0
    score = 0
    lifes = 3
    #Iniciamos la ventana
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("DODGER")
    pj = clases.dodgy(350,470,"cuadradoamarillo.jpg")

    while(not gameover):

        for event in pygame.event.get():
            #pulsar la x para salir
            if event.type == pygame.QUIT:
                gameover = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pj.posx = pj.posx - 5

                if event.key == pygame.K_RIGHT:
                    pj.posx = pj.posx + 5

                if event.key == pygame.K_UP:
                    pj.posy = pj.posy - 5

                if event.key == pygame.K_DOWN:
                    pj.posy = pj.posy + 5

        screen.fill((255,255,255))
        mostrar_imagen(screen, pj)
        spawn()
        for enem in enemigos:
            if(colision(enem,pj)):
                lifes -= 1
                print(lifes)
                if(lifes<=0):
                    gameover = True
            if(enem.posy >= 536):
                enem.posy = 536
                enem.impulso = 0
            muerte_enemigo(enem)
            mostrar_imagen(screen,enem)
            enem.posy = enem.posy + enem.impulso



        pygame.display.update()

main()
