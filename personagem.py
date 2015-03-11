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
    gravidade_level = 450
    walking_frames_r = []
    walking_frames_l = []
    fundo = pygame.image.load("img/sayonara.png")
    nivel = 3
    pos_x = 0 
    pos_y = 400
    window = pygame.display.set_mode((800, 600))
    sprite_sheet = SpriteSheet("img/personagem/p1_walk.png")
    image = sprite_sheet.get_image(0, 0, 66, 90)
    walking_frames_r.append(image)
    image = sprite_sheet.get_image(132, 0, 67, 90)
    walking_frames_r.append(image)
    image = sprite_sheet.get_image(0, 0, 66, 90)
    image = pygame.transform.flip(image, True, False)
    walking_frames_l.append(image)
    image = sprite_sheet.get_image(132, 0, 67, 90)
    image = pygame.transform.flip(image, True, False)
    walking_frames_l.append(image)
    walking_frames = walking_frames_r
    back_x = 0
    vida = 3
    personagem_imagem = walking_frames[0]
    vida_imagem = pygame.image.load("img/personagem/vida_3.png")
    vida_imagem.set_colorkey(0, 0)
    
    def _init_(self):
        pos_y = self.gravidade()
    
    def perdeVida(self):
        self.vida -= 1
        if self.vida == 2:
            self.vida_imagem = pygame.image.load("img/personagem/vida_2.png")
        elif self.vida == 1:
            self.vida_imagem = pygame.image.load("img/personagem/vida_1.png")
        elif self.vida == 0:
            while True:
                derrota = pygame.image.load("img/game_over.png")
                self.window.blit(derrota, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click = True
                        time.sleep(0.2)
                        return
                    if event.type == pygame.QUIT:
                        sys.exit()
        self.vida_imagem.set_colorkey(0, 0)
            
    def atualizar_tela(self):
        self.window.blit(self.fundo, (self.back_x, 0))
        self.window.blit(self.vida_imagem, (0, 0))
        self.window.blit(self.personagem_imagem, (self.pos_x, self.pos_y))
        for inimigo in jogar.nivel.inimigos:
            self.window.blit(inimigo.img, (inimigo.pos_x, inimigo.pos_y))
        pygame.display.update()
    
    def perder(self):
        self.perdeVida()
        if self.vida == 0:
            return
        for i in range(10):
            self.pos_y -= 10
        self.personagem_imagem = pygame.image.load("img/personagem/p1_hurt.png")
        while self.pos_y != self.gravidade_level:
                        self.pos_y += 10
                        self.atualizar_tela()
        self.personagem_imagem = self.walking_frames[0]
        self.pos_y = 0
        time.sleep(0.5)
        self.pos_x = 1
        self.back_x = 0
        self.gravidade() 
        pygame.display.update()
    
    def mover_fundo(self, qntde):
        self.window.blit(self.fundo, (self.back_x - 800, 0))
        self.back_x += qntde
        
    def mover_personagem(self, qntde):
        self.pos_x += qntde
        self.personagem_imagem = self.walking_frames[1]
        self.atualizar_tela()
        for inimigo in jogar.nivel.inimigos:
            inimigo.andar(self.window)
        time.sleep(0.06) 
        self.pos_x += qntde
        self.gravidade()
        self.atualizar_tela()
        self.personagem_imagem = self.walking_frames[0]
            
    def direita(self):
        self.walking_frames = self.walking_frames_r
        if (self.bateu('d') == True):
            return
        if (self.pos_x <=  self.fundo.get_height()):
            self.mover_fundo(-10)
            self.mover_personagem(5)
        elif (self.nivel == 1):
            self.nivel = 2
            jogar.nivel = jogar.Nivel2()
            jogar.preNivel(self.window)
            self.pos_x = 0
            self.pos_y = 360
            self.back_x = 0
            self.fundo = pygame.image.load(jogar.Nivel2.bg)
            pygame.display.update()
        elif (self.nivel == 2):
            self.nivel = 3
            jogar.nivel = jogar.Nivel3()
            jogar.preNivel(self.window)
            self.pos_x = 0
            self.pos_y = 400
            self.gravidade_level = 400
            self.back_x = 0
            self.fundo = pygame.image.load(jogar.Nivel3.bg)
            pygame.display.update()
            
        elif (self.nivel == 3):
             self.vida = 0
             while True:
                vitoria = pygame.image.load("img/win.png")
                self.window.blit(vitoria, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click = True
                        time.sleep(0.2)
                        return
                    if event.type == pygame.QUIT:
                        sys.exit()
             
            

    def esquerda(self):
        self.walking_frames = self.walking_frames_l
        if (self.bateu('e') == True):
            return
        if (self.pos_x >= 0):
            self.mover_fundo(10)
            self.mover_personagem(-5)

    def pular(self):
        for i in range(10):
            self.pos_y -= 10
            for inimigo in jogar.nivel.inimigos:
                inimigo.andar(self.window)
            self.atualizar_tela()
        self.gravidade()
            

        
    def pular_direita(self):
        self.walking_frames = self.walking_frames_r
        for i in range(5):
           self.pos_y -= 20
           self.pos_x += 10
           for inimigo in jogar.nivel.inimigos:
                inimigo.andar(self.window)
           self.atualizar_tela()
        self.mover_fundo(-50)
        self.gravidade()
    
    def pular_esquerda(self):
        self.walking_frames = self.walking_frames_l
        for i in xrange(5):
            self.pos_y -= 20
            self.pos_x -= 10
            for inimigo in jogar.nivel.inimigos:
                inimigo.andar(self.window)
            self.atualizar_tela()
        self.mover_fundo(50)
        self.gravidade()
        
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
        print self.pos_x, self.pos_y
        aux = self.pos_y
        for i in range(len(jogar.nivel.platforms)):
            self.pos_y = aux
            while (self.pos_y != self.gravidade_level):
                if((jogar.nivel.platforms[i][0] == self.pos_y) and ((jogar.nivel.platforms[i][1] <= self.pos_x) and (jogar.nivel.platforms[i][2] >= self.pos_x))): 
                    aux2 = aux
                    aux = self.pos_y
                    self.pos_y = aux2
                    print self.pos_y
                    while self.pos_y != aux:
                        self.pos_y += 10
                        self.atualizar_tela()
                    return
                self.pos_y += 10
        self.pos_y = aux 
        while self.pos_y != self.gravidade_level:
                        self.pos_y += 10
                        self.atualizar_tela()
        for i in range(len(jogar.nivel.buracos)):
            if ((jogar.nivel.buracos[i][0] <= self.pos_x) and (jogar.nivel.buracos[i][1] >= self.pos_x)):
                self.perder()
