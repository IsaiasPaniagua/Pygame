from ast import While
import pygame, sys, random

pygame.init()

#Definicion de colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
#Variables
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Definimos la visibilidad del mouse
pygame.mouse.set_visible(0)

#coordenadas del cuadrado
coord_x = 10
coord_y = 10
#Velocidad
speed_x = 0
speed_y = 0

while True:
    #Cerrar videojuego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Tecla Flecha izquierda
                speed_x = -3
            if event.key == pygame.K_RIGHT: #Tecla Flecha derecha
                speed_x = 3
            if event.key == pygame.K_UP: #Tecla Flecha arriba
                speed_y = -3
            if event.key == pygame.K_DOWN: #Tecla Flecha abajo
                speed_y = 3

        #Evento para cuando dejemos de presionar la tecla se quede en un lugar estatico
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: #Tecla Flecha izquierda
                speed_x = 0
            if event.key == pygame.K_RIGHT: #Tecla Flecha derecha
                speed_x = 0
            if event.key == pygame.K_UP: #Tecla Flecha arriba
                speed_y = 0
            if event.key == pygame.K_DOWN: #Tecla Flecha abajo
                speed_y = 0

    #nos da la posicion del mouse en tupla
    # mouse_pos = pygame.mouse.get_pos() 
    # x = mouse_pos[0]
    # y = mouse_pos[1]

    #Asigamos un color de fondo
    screen.fill(white)

    coord_x += speed_x
    coord_y += speed_y

    pygame.draw.rect(screen, red, (coord_x, coord_y, 100, 100))

    #Actualizamos la pantalla
    pygame.display.flip()
    clock.tick(60)