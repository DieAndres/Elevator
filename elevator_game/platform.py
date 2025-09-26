# core/platform.py
import pygame
from .config import *
from engine.game_object import GameObject 

class Platform(GameObject):
    def __init__(self, x, y, ancho, alto):
        """Inicializa una plataforma con su posición y tamaño."""
        super().__init__(
            x,  
            y,
            '',
            ancho,
            alto
        )        
    
    def dibujar(self, superficie):
        """Dibuja la plataforma en la pantalla."""
        pygame.draw.rect(superficie, GRIS, self.rect)