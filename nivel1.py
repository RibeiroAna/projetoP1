import pygame

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
    pos_x = 0 
    pos_y = 450

    window = pygame.display.set_mode((800, 600))
    sprite_sheet = SpriteSheet("img/p1_walk.png")
    image = sprite_sheet.get_image(0, 0, 66, 90)
    walking_frames_r.append(image)
    image = sprite_sheet.get_image(132, 0, 67, 90)
    walking_frames_r.append(image)
	
	    
    def direita(self):
		self.pos_x += 5
		window.blit(fundo, (x, 0))
		window.blit(player.walking_frames_r[1], (player.pos_x, player.pos_y))
		pygame.display.update()
		time.sleep(0.05)
		window.blit(fundo, (x, 0))
		self.pos_x += 5
		window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
		pygame.display.update()
    
    def esquerda(self):
        self.pos_x -= 10
        
    def cima(self):
        self.pos_y -= 100
        window.blit(fundo, (x, 0))
        pygame.display.update()
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        pygame.display.update()
        player.baixo()
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        time.sleep(0.3)
        window.blit(fundo, (x, 0))
        pygame.display.update()
        
   
    def baixo(self):
		while self.pos_y != 450:
			self.pos_y += 10

class nivel1:
	bg1 = "img/sayonara.png"
 
	def main():
		pygame.init()
		player = Personagem()
		fundo = pygame.image.load(bg1)
		window = pygame.display.set_mode((800, 600))
		pygame.key.set_repeat(1, 200)
		window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
		window.blit(fundo, (0, 0))
		x = 0
		while True:
			window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
			for event in pygame.event.get():
				 if event.type == pygame.QUIT:
					 sys.exit()
			         elif event.type == pygame.KEYDOWN:
			              if event.key == pygame.K_LEFT:
			    	         if (player.pos_x != 0):
				    	         window.blit(fundo, (x - 800, 0))
				    	         window.blit(fundo, (x, 0))
				    	         x += 10
				    	         player.esquerda()
			                 if event.key == pygame.K_RIGHT:
				                if (player.pos_x != 800):
					                player.direita()
					                window.blit(fundo, (x - 800, 0))
					                window.blit(fundo, (x, 0))
					                x -= 10
			                 if event.key == pygame.K_UP:
				                  player.cima()
			pygame.display.update()
             
nivel = nivel1()
nivel1.main()
