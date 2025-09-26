# core/enemy.py
import pygame
from .config import *
from .bullet import Bullet
from engine.game_object import GameObject

class Enemy(GameObject):
    def __init__(self, plataforma, x_inicial,image):
        """Inicializa al enemigo en una posición específica con un rango de patrullaje."""
        
        super().__init__(
            x_inicial,  
            '',
            image,
            64,
            64
        )
        #aca no le coloco eje y por que se coloca arriba de la plataforma que es lo que da la posicion del eje y        
        self.rect.x = x_inicial
        self.rect.bottom = plataforma.rect.top
        self.plataforma_actual = plataforma
        self.velocidad_x = VELOCIDAD_ENEMIGO

        # Lógica de disparo
        self.ultimo_disparo = pygame.time.get_ticks() # Tiempo del último disparo
        self.intervalo_disparo = 1000 # 3000 milisegundos = 3 segundos        

    def actualizar(self):
        """Actualiza la posición del enemigo y su patrón de movimiento."""
        self.rect.x += self.velocidad_x
        
        # Invertir la dirección si el enemigo llega a los bordes de la plataforma
        if self.rect.right >= self.plataforma_actual.rect.right or \
        self.rect.left <= self.plataforma_actual.rect.left:
            self.velocidad_x *= -1

    def dibujar(self, superficie):
        """Dibuja al enemigo en la pantalla."""
        superficie.blit(self.image, self.rect)

    def disparar(self, balas_enemigo):
        """Dispara una bala si ha pasado el tiempo."""
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_disparo > self.intervalo_disparo:
            self.ultimo_disparo = ahora
            if self.velocidad_x >= 0:
                direccion = 1
            else:
                direccion = -1           
            bala_nueva = Bullet(self.rect.centerx, self.rect.centery, direccion)
            balas_enemigo.append(bala_nueva)