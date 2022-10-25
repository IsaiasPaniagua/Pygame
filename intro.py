from ctypes.wintypes import tagMSG
import pygame, sys
pygame.init() #inicializamos pygame

#Definicion de colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

size = (800, 500)

#Crear ventana
screen = pygame.display.set_mode(size)

#Controla los FPS
clock = pygame.time.Clock()

#Coordenadas del cuadrado
cord_x = 400
cord_y = 200

#velocidad en la que se movera
speed_x = 1
speed_y = 1

while True:
    for event in pygame.event.get(): #registramos todos los eventos que sucedan en la ventana
        if event.type == pygame.QUIT:
            sys.exit()

    #Rebotes en la ventana
    if(cord_x > 720 or cord_x < 0):
        speed_x *= -1 
    if(cord_y > 420 or cord_y < 0):
        speed_y *= -1

    #Animacion para que nuestro cuadro se mueva
    cord_x += speed_x
    cord_y += speed_y

    #Color de fondo
    screen.fill(white) 
    
    #Zona de dibujo
    # En donde dibujaremos   color   inicio    fin     grosor
    # pygame.draw.line(screen, green, [0, 100], [100,100], 5) #Creamos una linea
    # pygame.draw.rect(screen, red, (100, 100, 80, 80)) #Creamos un cuadrado
    # pygame.draw.circle(screen, blue, (200, 200),5) #Creamos un circulo
    
    # for x in range(100, 400, 100): Dibujar figuras con un ciclo
    #     pygame.draw.rect(screen, black, (x, 230, 50, 50))
    #     pygame.draw.line(screen, green, (x, 0), (x, 100), 5)

    pygame.draw.rect(screen, red, (cord_x, cord_y, 80, 80))
    

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(80)