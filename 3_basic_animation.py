import pygame
from sys import exit   # Sirve para cerrar pygame


pygame.init()
screen = pygame.display.set_mode((800, 400))   # Tamaño de la ventana
pygame.display.set_caption('Runner')   # Nombre de la ventana
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)   # Creamos una fuente (font, size)


sky_surface = pygame.image.load('graphics/Sky.png').convert()   # Cargamos la imagen como una superficie
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Hello World', False, 'Black')   # Superficie con texto (texto, AA, color)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600


while True:   # Main loop
    for event in pygame.event.get():   # Read event
        if event.type == pygame.QUIT:   # Comprobar si event es igual a QUIT
            pygame.quit()   # Quit
            exit()   # Exit pygame
    
    screen.blit(sky_surface, (0, 0))   # Colocar test_surface sobre screen en la posicion (0, 0)
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 2
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    
    pygame.display.update()   # Update the display
    clock.tick(60)   # Esto hara que el while loop no se ejecute mas rapido que 60 vecex por segundo