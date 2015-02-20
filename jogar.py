#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém os níveis e o que detecta que os   #
# comandos do teclado.                                   #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   

import pygame, sys, time, personagem

 
class Nivel1():
    bg = "img/sayonara.png"

class Nivel2():
    #fundo provisório =P =V
    bg = "pessoasbugadas.jpg"
    
        
nivel = Nivel1()        

def jogar():
    window = pygame.display.set_mode((800, 600)) 
    pygame.init()
    player = personagem.Personagem()
    pygame.init()
    fundo = pygame.image.load(nivel.bg)
    
    #O segundo parâmetro da função define o delay das teclas.
    pygame.key.set_repeat(10, 20) 
    
    window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
    window.blit(fundo, (0, 0))
    
    # botao que define a pausa (por enquanto voltando para o menu)
    pausa = False
    # carrega música
    musica_principal = pygame.mixer.Sound('sound/musica_principal.ogg')
    volume_principal = 0.01
    musica_principal.set_volume(volume_principal)
    while True:
        if pausa == True:
            break
        
        # começa a tocar a música e define o volume.
        musica_principal.play(-1)
        
        pygame.mouse.set_visible(False)
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    musica_principal.stop()
                    pausa = True
                if event.key == pygame.K_LEFT:
                    player.esquerda()
                if event.key == pygame.K_RIGHT:
                    player.direita()
                if event.key == pygame.K_UP:
                    player.cima()
                
        pygame.display.update()
