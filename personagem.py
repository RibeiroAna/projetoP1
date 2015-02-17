#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém tudo que se refere ao personagem e #
# que é necessário para o seu funcionamento, desde os    #
# movimentos até cortar o sprite                         #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   

import pygame, time

class SpriteSheet(object):
    sprite_sheet = None
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(0, 0)
        return image


class Personagem():
    walking_frames_r = []
    fundo = pygame.image.load("img/sayonara.png")
    pos_x = 0 
    pos_y = 450
    window = pygame.display.set_mode((800, 600))
    sprite_sheet = SpriteSheet("img/p1_walk.png")
    image = sprite_sheet.get_image(0, 0, 66, 90)
    walking_frames_r.append(image)
    image = sprite_sheet.get_image(132, 0, 67, 90)
    walking_frames_r.append(image)
    back_x = 0
    
    def mover_fundo(self, qntde):
		self.window.blit(self.fundo, (self.back_x - 800, 0))
		self.window.blit(self.fundo, (self.back_x, 0))
		self.back_x += qntde
		
    def mover_personagem(self, qntde):
        self.pos_x += qntde
        self.window.blit(self.fundo, (self.back_x, 0))
        self.window.blit(self.walking_frames_r[1], (self.pos_x, self.pos_y))
        pygame.display.update()
        time.sleep(0.06)
        self.window.blit(self.fundo, (self.back_x, 0))
        self.pos_x += qntde
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        pygame.display.update()
            
    def direita(self):
		if (self.pos_x <=  self.fundo.get_height()):
			self.mover_fundo(-10)
			self.mover_personagem(5)
        #Senão mude de fase, à implementar

    def esquerda(self):
		if (self.pos_x >= 0):
		    self.mover_fundo(10)
		    self.mover_personagem(-5)

    def cima(self):
        self.pos_y -= 100
        self.window.blit(self.fundo, (self.back_x, 0))
        pygame.display.update()
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        pygame.display.update()
        self.baixo()
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        time.sleep(0.3)
        self.window.blit(self.fundo, (self.back_x, 0))
        pygame.display.update()


    def baixo(self):
        while self.pos_y != 450:
            self.pos_y += 10
