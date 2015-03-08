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
pygame.mixer.init()
somDeClick = pygame.mixer.Sound('sound/click.wav')
somDeClick.set_volume(volume.volume_efeitos)

def preNivel(window):
    click = False
    telas = 1
    while True:
        #Pre fase
        if telas == 1:
           window.blit(pygame.image.load(nivel.preFase), (0, 0))
           pygame.display.update()
           
        if click and telas == 2:
            return
        if click:
            print click, telas
            telas = 2
            #Missão
            window.blit(pygame.image.load(nivel.missao), (0, 0))
            pygame.display.update()
            click = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                time.sleep(0.2)
            if event.type == pygame.QUIT:
                sys.exit()
            
    
 
#Provavelmente estes níveis irão para outro arquivo, mas provisiorialmente, aqui
class Nivel1():
    preFase = "img/preFase1.png"
    missao = "img/missao1.png"
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
    bg = "img/laguinho.png"
    preFase = "img/preFase2.png"
    missao = "img/missao2.png"
    platforms = [[360, 0, 50, 450], [360, 90, 120, 450], [360, 160, 200, 450], [290, 200, 240, 360], [220, 270, 370, 360], [290, 400, 440, 450], [220, 470, 510, 450], [360, 540, 580, 450]]
    buracos = [[50, 540]]
    peixe = inimigo.Peixe()
    peixe.def_x_y_dirp(300, 570, -0.5)
    peixe1 = inimigo.Peixe()
    peixe1.def_x_y_dirp(500, 400, 1.)
    peixe2 = inimigo.Peixe()
    peixe2.def_x_y_dirp(175, 100, -0.75)
    inimigos = [peixe, peixe1, peixe2]
    
class Nivel3():
    bg = "img/spLab.png"
    #Provisorios
    preFase = "img/preFase3.png"
    missao = "img/missao3.png"
    platforms = [[400, 0, 90, 450], [310, 90, 160, 450], [400, 190, 240, 400], ]
    buracos = [[90,180]]
    inimigos = []
        
nivel = Nivel1()    
player = personagem.Personagem()
    
def jogar(window_pric):
    window = window_pric
    preNivel(window)
    fundo = pygame.image.load(nivel.bg)
    
    #O segundo parâmetro da função define o delay das teclas.
    pygame.key.set_repeat(10, 30) 
    
    window.blit(player.walking_frames[0], (player.pos_x, player.pos_y))
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
        if player.vida == 0:
            break
        # começa a tocar a música e define o volume.
        musica_principal.play(-1)
        
        window.blit(player.walking_frames[0], (player.pos_x, player.pos_y))
        
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
                    player.pular()
                if event.key == pygame.K_SPACE:
                    player.pular_direita()
                if event.key == pygame.K_c:
                    player.pular_esquerda()
                
        pygame.display.update()
