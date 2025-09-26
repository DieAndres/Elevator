# core/player.py
import pygame
from .config import *
from engine.game_object import GameObject

class Player(GameObject):
    def __init__(self, image_sprite): 
        """Inicializa el personaje."""    
        #self.rect.center = (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2)
        # Variables de movimiento y salto
        super().__init__(
            x=ANCHO_PANTALLA/2 - 32,  
            y=ALTO_PANTALLA/2 - 32,
            image=image_sprite,
            width=64,
            height=64
        )
        self.velocidad = VELOCIDAD_JUGADOR
        self.velocidad_y = 0
        self.en_el_suelo = False
        self.disparando = False
       
    def actualizar(self, plataformas):
        """Actualiza la posición y el estado del personaje."""
        # Aplicar gravedad
        self.velocidad_y += GRAVEDAD
        self.rect.y += self.velocidad_y

        # Manejar colisiones con las plataformas
        self.en_el_suelo = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                # Si el personaje está cayendo sobre la plataforma (aterrizaje)
                if self.velocidad_y >= 0:
                    self.rect.bottom = plataforma.rect.top
                    self.velocidad_y = 0
                    self.en_el_suelo = True
                # Cuando colisiona contra una plataforma y su velocidad es  menor a 0 es por que esta subiendo y 
                # choca contra una plataforma que esta arriba
                elif self.velocidad_y < 0:
                    self.rect.top = plataforma.rect.bottom
                    self.velocidad_y = 0

    def mover(self, teclas):
        """Maneja el movimiento horizontal y el salto."""
        # Movimiento horizontal
        self.rect.x += 0
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        
        # Salto
        if teclas[pygame.K_UP] and self.en_el_suelo:
            self.velocidad_y = -10 # Un valor negativo para ir hacia arriba
            self.en_el_suelo = False
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA
                