#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém os níveis e o que detecta que os   #
# comandos do teclado.                                   #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   

import pygame, sys, time, personagem, inimigo

class Volume:
    volume_musica = 0.03
    volume_efeitos = 1.
    def mudaVolumeMusica(self, valor):
        self.volume_musica = valor
    def mudaVolumeEfeitos(self, valor):
        self.volume_efeitos = valor

volume = Volume()
 
#Provavelmente estes níveis irão para outro arquivo, mas provisiorialmente, aqui
class Nivel1():
    bg = "img/sayonara.png"
    #A matriz representa o local dos blocos, a ordem é [y1, x1, x2, y2], por que é nessa ordem?
    #como diria Joseana, porque sim, foi a "equipe" de "engenheiros" que projetou que quiz assim
    platforms = [[390, 25, 90, 450], [390, 125, 190, 450], [320, 200, 255, 390], [390, 255, 370, 450], [320, 380, 410, 390], [260, 420, 470, 280], [390, 500, 700, 450]]
    #Esta matriz representa os buracos, onde [x1, x2], indicando onde começa e termina tais ítens
    buracos = [[90, 200], [410, 500]]
    #Esta matriz representa os inimigos
    mosca = inimigo.Mosca()
    mosca.def_x_y_dir(0, 320, -0.5)
    mosca1 = inimigo.Mosca()
    mosca1.def_x_y_dir(300, 390, 0.5)
    mosca2 = inimigo.Mosca()
    mosca2.def_x_y_dir(500, 260, -0.5)
    inimigos = [mosca1, mosca2, mosca]
    

class Nivel2():
    #fundo provisório =P =V
    bg = "pessoasbugadas.jpg"
    platforms = [[0,0,0]]
    buracos = []
        
nivel = Nivel1()    
player = personagem.Personagem()
    
def jogar(window_pric):
    window = window_pric
    fundo = pygame.image.load(nivel.bg)
    
    #O segundo parâmetro da função define o delay das teclas.
    pygame.key.set_repeat(10, 30) 
    
    window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
    window.blit(fundo, (0, 0))    
    # botao que define a pausa (por enquanto voltando para o menu)
    pausa = False
    # carrega música
    musica_principal = pygame.mixer.Sound('sound/musica_principal.ogg')
    musica_principal.set_volume(volume.volume_musica)
    while True:
        player.atualizar_tela()
        for inimigo in nivel.inimigos:
			inimigo.andar(window)
        if pausa == True:
            break
        
        # começa a tocar a música e define o volume.
        #musica_principal.play(-1)
        
        pygame.mouse.set_visible(False)
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    musica_principal.stop()
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
