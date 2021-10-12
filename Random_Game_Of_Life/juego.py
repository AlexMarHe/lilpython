import pygame as py
import numpy as np
import time

#calcula las nuevas celulas tras 1 iteracion hay que hacer la copia en una nueva matriz ya que si por ejemplo cambiamos la celula (1,1) el calculo de (1,2) se vería afectado
#en esa misma llamada de calculo_matriz.
def calculo_matriz(matriz):
    sum=0
    matriz_nueva = np.zeros((tam_matriz,tam_matriz))
    for i in range(0,tam_matriz):
        for j in range(0,tam_matriz):
            sum = matriz[(i-1) % tam_matriz,(j+1) % tam_matriz]+matriz[i % tam_matriz, (j+1) % tam_matriz]+matriz[(i+1) % tam_matriz,(j+1) % tam_matriz] + matriz[(i+1) % tam_matriz, j % tam_matriz]+matriz[(i+1) % tam_matriz,(j-1) % tam_matriz]
            sum += matriz[(i-1) % tam_matriz,j % tam_matriz]+matriz[i % tam_matriz,(j-1) % tam_matriz]+matriz[(i-1) % tam_matriz,(j-1) % tam_matriz]

            if matriz[i, j] == 0 :
                if sum == 3:
                    matriz_nueva[i,j] = 1
            '''else:
                if sum < 2 or sum > 3:
                    matriz_nueva[i,j] = 0
            sum=0'''
    return matriz_nueva

#imprime las células en la pantalla a partir de la matriz
def imprimir_celulas(matriz, screen, viva, muerta):
    for i in range(0,tam_matriz):
        for j in range(0,tam_matriz):
            if(matriz[i, j] == 1):
                screen.blit(viva,(i*50,j*50))
            else:
                screen.blit(muerta,(i*50,j*50))

#iniciamos pygame
py.init()

#variables numéricas
tam_x, tam_y = 1000, 1000
tam_cel = 50
tam_matriz = int(tam_x/tam_cel)
running = True

#creamos una matriz aleatoria para representar las celulas con 1000/50 celulas cada fila y columna
matriz = np.random.choice([0,1], size=(int(tam_x/tam_cel),int(tam_y/tam_cel)), p=[.7,.3])

#variables(objetos) de pygame
screen = py.display.set_mode((tam_x,tam_y))
viva = py.image.load("viva.jpg")
muerta = py.image.load("muerta.jpg")

while(running):

    for event in py.event.get():
        if event.type == py.QUIT:
            running=False

    matriz = calculo_matriz(matriz)
    imprimir_celulas(matriz, screen, viva, muerta)
    py.display.update()
    time.sleep(2)
