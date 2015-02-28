#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém tudo que se refere ao personagem e #
# que é necessário para o seu funcionamento, desde os    #
# movimentos até cortar o sprite                         #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   

import pygame, time, jogar

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
    nivel = 1
    pos_x = 0 
    pos_y = 450
    window = pygame.display.set_mode((800, 600))
    sprite_sheet = SpriteSheet("img/personagem/p1_walk.png")
    image = sprite_sheet.get_image(0, 0, 66, 90)
    walking_frames_r.append(image)
    image = sprite_sheet.get_image(132, 0, 67, 90)
    walking_frames_r.append(image)
    back_x = 0
    vida = 3
    personagem_imagem = walking_frames_r[0]
    vida_imagem = pygame.image.load("img/personagem/vida_3.png")
    vida_imagem.set_colorkey(0, 0)
    
    def perdeVida(self):
        self.vida -= 1
        if self.vida == 2:
            self.vida_imagem = pygame.image.load("img/personagem/vida_2.png")
        elif self.vida == 1:
            self.vida_imagem = pygame.image.load("img/personagem/vida_1.png")
        elif self.vida == 0:
            #Tela de derrota provisoriaa
            self.vida_imagem = pygame.image.load("pessoasbugadas.jpg")
        self.vida_imagem.set_colorkey(0, 0)
            
    def atualizar_tela(self):
        self.window.blit(self.fundo, (self.back_x, 0))
        self.window.blit(self.vida_imagem, (0, 0))
        self.window.blit(self.personagem_imagem, (self.pos_x, self.pos_y))
        pygame.display.update()
    
    def volta_inicio(self):
        self.perdeVida()
        time.sleep(0.5)
        self.pos_x = 0 
        self.pos_y = 450
        self.back_x = 0
        pygame.display.update()
    
    def mover_fundo(self, qntde):
        self.window.blit(self.fundo, (self.back_x - 800, 0))
        self.back_x += qntde
        
    def mover_personagem(self, qntde):
        self.pos_x += qntde
        self.personagem_imagem = self.walking_frames_r[1]
        self.atualizar_tela()
        time.sleep(0.06) 
        self.pos_x += qntde
        self.gravidade()
        self.atualizar_tela()
        self.personagem_imagem = self.walking_frames_r[0]
            
    def direita(self):
        if (self.bateu('d') == True):
            return
        if (self.pos_x <=  self.fundo.get_height()):
            self.mover_fundo(-10)
            self.mover_personagem(5)
        elif (self.nivel == 1):
            self.nivel = 2
            jogar.nivel = jogar.Nivel2()
            self.pos_x = 0
            self.back_x = 0
            self.fundo = pygame.image.load(jogar.Nivel2.bg)
            pygame.display.update()

    def esquerda(self):
        if (self.bateu('e') == True):
            return
        if (self.pos_x >= 0):
            self.mover_fundo(10)
            self.mover_personagem(-5)

    def pular(self):
        self.pos_y -= 100
        self.atualizar_tela()
        self.gravidade()
        self.atualizar_tela()
        time.sleep(0.3)
        self.atualizar_tela()

        
    def pular_direita(self):
        self.pos_y -= 100
        self.pos_x += 50
        self.mover_fundo(-50)
        time.sleep(0.3)
        self.gravidade()
        self.atualizar_tela()
        
    def bateu(self,lado):
        #Mindica esquerda, verificando se há algo a esquerda
        if (lado == 'e'):
            for i in range(len(jogar.nivel.platforms)):
                if jogar.nivel.platforms[i][2] >= self.pos_x:
                    if not(jogar.nivel.platforms[i][0] >= self.pos_y):
                        if not(jogar.nivel.platforms[i][0] == self.pos_y):
                            if jogar.nivel.platforms[i][1] <= self.pos_x:
                                return True
        else:
            #Verificando se há algo a direita
            for i in range(len(jogar.nivel.platforms)):
                if (self.pos_x -jogar.nivel.platforms[i][1] > -25):
                    if not(jogar.nivel.platforms[i][0] >= self.pos_y):
                        if not(jogar.nivel.platforms[i][0] >= self.pos_y):
                            if not(jogar.nivel.platforms[i][0] == self.pos_y):
                                if (self.pos_x -jogar.nivel.platforms[i][1] < 0):
                                    return True
        return False
        
   
    def gravidade(self):
        aux = self.pos_y
        for i in range(len(jogar.nivel.platforms)):
            self.pos_y = aux
            while (self.pos_y != 450):
                print i, len(jogar.nivel.platforms), self.pos_y
                if((jogar.nivel.platforms[i][0] == self.pos_y) and ((jogar.nivel.platforms[i][1] <= self.pos_x) and (jogar.nivel.platforms[i][2] >= self.pos_x))): 
                    return
                self.pos_y += 10
        print i
        self.pos_y = 450
        for i in range(len(jogar.nivel.buracos)):
            if ((jogar.nivel.buracos[i][0] <= self.pos_x) and (jogar.nivel.buracos[i][1] >= self.pos_x)):
                self.volta_inicio()
