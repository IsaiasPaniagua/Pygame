import pygame, sys, random
pygame.init()

#Definicion de colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Variables
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []

#For para dibujar 60 circulos en la ventana
for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        #Agregamos las coordenadas de los puntos en nuestra lista
        coor_list.append([x, y]) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #Zona de animación

    
    #Color de fondo
    screen.fill(white) 

    #Zona de dibujo
    for coord in coor_list:
        # x = coord[0]
        # y = coord[1]
        pygame.draw.circle(screen, red, coord, 2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0


    #Actualizamos la pantalla
    pygame.display.flip() 
    clock.tick(30)