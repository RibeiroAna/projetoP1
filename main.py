import pygame, sys

pygame.init()
pygame.display.set_caption('UFCG: the journey!')
window = pygame.display.set_mode((800, 600))

# variaveis relacionadas o menu
white = (255, 255, 255)
menu = 0
menu0 = pygame.image.load('img/menu/tela0.png')
menu0_select = pygame.image.load('img/menu/tela0Select.png')
menu1 = pygame.image.load('img/menu/tela1.png')
select = pygame.image.load('img/menu/seta_menu.png')
sair = pygame.image.load('img/menu/sair.png')

while True:
    # variaveis do mouse
    click = pygame.mouse.get_pressed()[0]
    mouse_pos_x = pygame.mouse.get_pos()[0]
    mouse_pos_y = pygame.mouse.get_pos()[1]
    
    # menu inicial - 0 
    if menu == 0:
        window.blit(menu0, (0, 0))
        
        if (220 < mouse_pos_x < 440 and 160 < mouse_pos_y < 480) and menu == 0:
            window.blit(menu0_select, (0, 0))
            if click:
                menu += 1
    
    # menu principal
    if menu == 1:
        window.blit(menu1, (0, 0))
        print (mouse_pos_x, mouse_pos_y)
        if mouse_pos_x > 583:
            # Captura mouse - botao jogar
            if 348 < mouse_pos_y < 378:
                window.blit(select, (543, 358))
            # Captura mouse - botao ajustes
            elif 433 < mouse_pos_y < 478:
                window.blit(select, (543, 443))
            # Captura mouse - botao creditos
            elif 517 < mouse_pos_y < 560:
                window.blit(select, (543, 533))
        elif 517 < mouse_pos_y < 560:
            # Captura mouse - botao sair
            if 192 < mouse_pos_x < 314:
                window.blit(select, (147, 533))
                if click:
                    menu = -1
	# menu sair
    if menu == -1:
        window.blit(sair, (0, 0))
        # Captura mouse - jogar mais
        if 254 < mouse_pos_x < 731 and 445 < mouse_pos_y < 517:
            window.blit(select, (214, 475))
            if click:
                menu = 1
        # Captura mouse - sair
        elif 9 < mouse_pos_x < 140 and 129 < mouse_pos_y < 585:
            if click:
                sys.exit()
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.update()
    
    
