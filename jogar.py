#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém os níveis e o que detecta que os   #
# comandos do teclado.                                   #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   

import pygame, sys, time, personagem

#Provavelmente estes níveis irão para outro arquivo, mas provisiralmente, aqui
class Nivel1():
    bg = "img/sayonara.png"
    #A matriz representa o local dos blocos, a ordem é [y1, x1, x2, y2], por que é nessa ordem?
    #como diria Joseana, porque sim, foi a "equipe" de "engenheiros" que projetou que quiz assim
    platforms = [[390, 25, 90, 450], [390, 125, 190, 450], [320, 200, 255, 390], [390, 255, 370, 450], [320, 380, 410, 390], [260, 420, 470, 280], [390, 500, 700, 450]]
    #Esta matriz representa os buracos, onde [x1, x2], indicando onde começa e termina tais ítens
    buracos = [[90, 200], [410, 500]]

class Nivel2():
	#fundo provisório =P =V
    bg = "pessoasbugadas.jpg"
    platforms = [[0,0,0]]
		
        
nivel = Nivel1()	

def jogar():
    window = pygame.display.set_mode((800, 600)) 
    pygame.init()
    player = personagem.Personagem()
    pygame.init()
    fundo = pygame.image.load(nivel.bg)
    
    #O segundo parâmetro da função define o delay das teclas.
    pygame.key.set_repeat(10, 30) 
    
    window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
    window.blit(fundo, (0, 0))    
    # botao que define a pausa (por enquanto voltando para o menu)
    pausa = False
    
    while True:
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        if pausa == True:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = True
                elif event.key == pygame.K_LEFT:
                    player.esquerda()
                elif event.key == pygame.K_RIGHT:
                    player.direita()
                elif event.key == pygame.K_UP:
                    player.pular()
                elif event.key == pygame.K_SPACE:
					player.pular_direita()
                
        pygame.display.update()
