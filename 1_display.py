import pygame
from sys import exit   # Sirve para cerrar pygame


pygame.init()
screen = pygame.display.set_mode((800, 400))   # Tamaño de la ventana
pygame.display.set_caption('Runner')   # Nombre de la ventana
clock = pygame.time.Clock()

while True:   # Main loop
    for event in pygame.event.get():   # Read event
        if event.type == pygame.QUIT:   # Comprobar si event es igual a QUIT
            pygame.quit()   # Quit
            exit()   # Exit pygame
    
    pygame.display.update()   # Update the display
    clock.tick(60)   # Esto hara que el while loop no se ejecute mas rapido que 60 vecex por segundo