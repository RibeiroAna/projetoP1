#coding: utf-8 
#----- Código do jogo "UFCG: The Journey ----------#
# Este arquivo contém tudo que se refere aos inimigos e #
# que é necessário para o seu funcionamento, desde os    #
# movimentos até cortar o sprite                         #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     # 

import pygame, personagem, jogar, time

class Inimigo():
      def colidir_inimigo(self, pos_x, pos_y):
         if ((pos_x >= jogar.player.pos_x - 55) and(pos_x <= jogar.player.pos_x + 55)   and (pos_y <= jogar.player.pos_y + 100) and (pos_y >= jogar.player.pos_y) ):
             print "morri por mosca"
             jogar.player.perder()

class Mosca():
    img = pygame.image.load("img/inimigos/fly1.png")
    pos_x = 0
    pos_y = 0
    direcao = 0
    def def_x_y_dir(self, pos_x, pos_y, direcao):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load("img/inimigos/fly1.png")
        self.direcao = direcao

        
    def andar(self, window):
        if ((self.pos_x <= 0) or (self.pos_x >= 800)):
            self.direcao = self.direcao*(-1)
        self.pos_x += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.pos_x += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
    
class Peixe():
    img = pygame.image.load('peixe.png')
    pos_x = 0
    pos_y = 0
    direcao = 0
    
    def def_x_y_dirp(self, pos_x, pos_y, direcao):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load('peixe.png')
        self.direcao = direcao
    
    def andar(self, window):
        if ((self.pos_y <= 0) or (self.pos_y >= 600)):
            self.direcao = self.direcao*(-1)
        self.pos_y += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.pos_y += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
