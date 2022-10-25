import pygame, sys, random

#Inicializamos pygame
pygame.init()

#Definicion de colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
#Variables
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_over = False
    #Coordenadas
coord_x_barra = 400 - 35
coord_y_barra = 585
cord_x_circle = 390
cord_y_circle = 50
    # Velocidades
speed_x_circle = 2
speed_y_circle = 2
speed_x_barra = 0


#Ciclo infinito
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        #Eventos para mover la barra
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Tecla Flecha izquierda
                speed_x_barra = -3
            if event.key == pygame.K_RIGHT: #Tecla Flecha derecha
                speed_x_barra = 3

        #Evento para cuando dejemos de presionar la tecla se quede en un lugar estatico
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: #Tecla Flecha izquierda
                speed_x_barra = 0
            if event.key == pygame.K_RIGHT: #Tecla Flecha derecha
                speed_x_barra = 0
        #Evento para que la barra no se salga de los limites de la pantalla
        if(coord_x_barra >750):
            coord_x_barra = 745
        elif(coord_x_barra < 0):
            coord_x_barra=5

    #Rebotes en la ventana
    if(cord_x_circle > 790 or cord_x_circle < 10):
        speed_x_circle *= -1 
    if(cord_y_circle > 590 or cord_y_circle < 10):
        speed_y_circle *= -1

    #Animacion para que nuestra pelota se mueva
    cord_x_circle += speed_x_circle
    cord_y_circle += speed_y_circle

    coord_x_barra += speed_x_barra

    #Asignamos color de fondo
    screen.fill(white)

    #Zona de dibujo
    pelota = pygame.draw.circle(screen, red, (cord_x_circle, cord_y_circle), 10)
    player = pygame.draw.rect(screen, green, (coord_x_barra, coord_y_barra, 90, 15))

    #Colisiones
    if pelota.colliderect(player):
        speed_x_circle *= -1

    #Actualizamos pantalla
    pygame.display.flip()
    clock.tick(60)