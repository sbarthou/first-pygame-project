import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('Hello World', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50)) 

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     print('key down')   # Imprime key down si se preciona una tecla
        # if event.type == pygame.KEYUP:
        #     print('key up')   # Imprime key up cuando se deja de presionar la tecla
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print('jump')   # Segundo metodo para saltar
            
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surf, score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    
    # keys = pygame.key.get_pressed()   # Array con ceros para las teclas no presionadas y un 1 para las teclas presionadas
    # if keys[pygame.K_SPACE]:
    #     print('jump')   # Primer metodo para saltar
    
    pygame.display.update()
    clock.tick(60)