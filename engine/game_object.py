# engine/game_object.py
import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width=None, height=None):
        super().__init__()
        if image != '':
            self.image = image
            self.image = pygame.transform.scale(image, (width, height)).convert_alpha()
            self.rect = self.image.get_rect()

        if image == '':
            self.rect = pygame.Rect(x, y, width, height)
        
        

    def dibujar(self, screen):
        screen.blit(self.image, self.rect)

    def actualizar(self):
        pass
