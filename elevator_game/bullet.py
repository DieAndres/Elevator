# core/bullet.py
import pygame
from .config import *
from engine.game_object import GameObject 

class Bullet(GameObject):
    def __init__(self, x, y, direccion):
        """Inicializa la bala con su posición y dirección."""
        self.image = pygame.Surface((10, 5))
        self.image.fill(BLANCO)        
        super().__init__(
            x,  
            y,
            self.image,
            10,
            5
        )     
        self.rect.centerx = x
        self.rect.centery = y
        self.velocidad_x = VELOCIDAD_BALA * direccion # La dirección será 1 o -1
    
    def actualizar(self):
        """Mueve la bala."""
        self.rect.x += self.velocidad_x

    def dibujar(self, superficie):
        """Dibuja la bala en la pantalla."""
        superficie.blit(self.image, self.rect)