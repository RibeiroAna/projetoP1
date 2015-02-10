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
    x = 0
            
    def direita(self):
        self.window.blit(self.fundo, (self.x - 800, 0))
        self.window.blit(self.fundo, (self.x, 0))
        self.x -= 10
        self.pos_x += 5
        self.window.blit(self.fundo, (self.x, 0))
        self.window.blit(self.walking_frames_r[1], (self.pos_x, self.pos_y))
        pygame.display.update()
        time.sleep(0.05)
        self.window.blit(self.fundo, (self.x, 0))
        self.pos_x += 5
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        pygame.display.update()

    def esquerda(self):
        self.window.blit(self.fundo, (self.x - 800, 0))
        self.window.blit(self.fundo, (self.x, 0))
        self.x += 10
        self.pos_x -= 5
        self.window.blit(self.walking_frames_r[1], (self.pos_x, self.pos_y))
        pygame.display.update()
        pygame.display.update()
        time.sleep(0.05)
        self.window.blit(self.fundo, (self.x, 0))
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        pygame.display.update()

    def cima(self):
        self.pos_y -= 100
        self.window.blit(self.fundo, (self.x, 0))
        pygame.display.update()
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        pygame.display.update()
        self.baixo()
        self.window.blit(self.walking_frames_r[0], (self.pos_x, self.pos_y))
        time.sleep(0.3)
        self.window.blit(self.fundo, (self.x, 0))
        pygame.display.update()


    def baixo(self):
        while self.pos_y != 450:
            self.pos_y += 10
