# /engine/game_loop.py
import pygame
import sys

class GameLoop:
    def __init__(self, title="Game", width=800, height=600):
        """
        Inicializa el bucle principal del juego, la ventana y el reloj.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """
        Ejecuta el bucle principal del juego.
        """
        while self.running:
            self.handle_events()
            self.update_game_logic()
            self.draw_game_elements()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        """
        Maneja los eventos del sistema (cerrar ventana, etc.).
        Este método llama a un método que el desarrollador debe sobrescribir.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.handle_specific_events(event)

    def handle_specific_events(self, event):
        """
        Método vacío que el desarrollador del juego debe sobrescribir
        para manejar la lógica de entrada específica del juego (ej. teclado).
        """
        pass

    def update_game_logic(self):
        """
        Método vacío que el desarrollador del juego debe sobrescribir
        para actualizar la lógica de movimiento, colisiones, etc.
        """
        pass

    def draw_game_elements(self):
        """
        Método vacío que el desarrollador del juego debe sobrescribir
        para dibujar todos los elementos en la pantalla.
        """
        pass