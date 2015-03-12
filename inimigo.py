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
            jogar.player.perder()
    
    def colidir_ajudante(self, pos_x, pos_y):
        if ((pos_x >= jogar.player.pos_x - 55) and(pos_x <= jogar.player.pos_x + 55)   and (pos_y <= jogar.player.pos_y + 100) and (pos_y >= jogar.player.pos_y) ):
            pass

class Mosca():
    img_l = pygame.image.load("img/inimigos/fly1.png")
    img_r = pygame.transform.flip(img_l, True, False)
    img = img_l
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
        if self.direcao < 0: self.img = self.img_l
        else: self.img = self.img_r
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.pos_x += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
    
class Peixe():
    img_up = pygame.image.load('img/inimigos/peixe.png')
    img_down = pygame.transform.flip(img_up, True, True)
    img = img_up
    pos_x = 0
    pos_y = 0
    direcao = 0
    
    def def_x_y_dirp(self, pos_x, pos_y, direcao):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load('img/inimigos/peixe.png')
        self.direcao = direcao
    
    def andar(self, window):
        if ((self.pos_y <= 0) or (self.pos_y >= 600)):
            self.direcao = self.direcao*(-1)
        if self.direcao < 0: self.img = self.img_up
        else: self.img = self.img_down
        self.pos_y += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.pos_y += self.direcao
        Inimigo().colidir_inimigo(self.pos_x, self.pos_y)
        
class GuardaChave():
    img_r = pygame.image.load("img/inimigos/klaudio.png")
    img_l = pygame.transform.flip(img_r, True, False)
    img = img_l
    pos_x = 0
    pos_y = 0
    direcao = 0
    def def_x_y_dir(self, pos_x, pos_y, direcao):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load("img/inimigos/klaudio.png")
        self.direcao = direcao
    
    def andar(self, window):
        if ((self.pos_x <= 0) or (self.pos_x >= 800)):
            self.direcao = self.direcao*(-1)
        self.pos_x += self.direcao
        if self.direcao < 0: self.img = self.img_l
        else: self.img = self.img_r
        Inimigo().colidir_ajudante(self.pos_x, self.pos_y)
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.pos_x += self.direcao
        Inimigo().colidir_ajudante(self.pos_x, self.pos_y)
