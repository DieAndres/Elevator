# core/game.py
import pygame
from .config import *
from engine.asset_manager import AssetManager
from .player import Player        
from .platform import Platform
from .enemy import Enemy
from engine.game_loop import GameLoop
import os # Necesitas esto para las rutas de los archivos
class ElevatorGame(GameLoop):
    def __init__(self):
        """Inicializa los componentes principales del juego."""
        super().__init__(title=TITULO_JUEGO, width=ANCHO_PANTALLA, height=ALTO_PANTALLA)
        #Cargar Imagenes     
        self.assets = AssetManager()
        self._load_assets()   
        #Player
        jugador_img = self.assets.get_image('jugador_sprite')
        self.jugador = Player(jugador_img)

        # Crear la lista de plataformas
        self.plataformas = []
        # Crear el piso principal
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 10, ANCHO_PANTALLA, 30))
        #Esto luego lo tendre que pasar a un for o algo por el estilo
        # Plataformas para el segundo piso
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 500, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(450, ALTO_PANTALLA - 500, ANCHO_PLATAFORMA, 20))
        # Plataformas para el tercer piso
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 400, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(450, ALTO_PANTALLA - 400, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 300, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(450, ALTO_PANTALLA - 300, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 200, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(450, ALTO_PANTALLA - 200, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(0, ALTO_PANTALLA - 100, ANCHO_PLATAFORMA, 20))
        self.plataformas.append(Platform(450, ALTO_PANTALLA - 100, ANCHO_PLATAFORMA, 20))

        #Enemigo
        self.enemigos = []                       
        plataforma_enemigo = self.plataformas[2] 
        enemigo_img = self.assets.get_image('enemigo_sprite')
        self.enemigos.append(Enemy(plataforma_enemigo, plataforma_enemigo.rect.x,enemigo_img))

        #Bala
        self.balas_enemigo = []           
    
    
    def handle_specific_events(self, event):
        # La clase GameLoop ya maneja el pygame.QUIT, así que no es necesario        
        pass

    def update_game_logic(self):
        """Actualiza la lógica del juego."""
        teclas = pygame.key.get_pressed()
        #Jugador
        self.jugador.mover(teclas)
        self.jugador.actualizar(self.plataformas)
        #Enemigo
        for enemigo in self.enemigos:
            enemigo.actualizar()
            enemigo.disparar(self.balas_enemigo)
        pass
        #Bala Enemigo
        for bala in self.balas_enemigo:
            bala.actualizar()
            if bala.rect.x < 0 or bala.rect.x > ANCHO_PANTALLA:
                self.balas_enemigo.remove(bala)
        
        for bala_enemigo in self.balas_enemigo:
            if self.jugador.rect.colliderect(bala_enemigo.rect):
                print("¡El jugador ha sido alcanzado!")
                self.running = False # Termina el juego

    def draw_game_elements(self):
        """Dibuja todos los elementos en la pantalla."""
        self.screen.fill(NEGRO)
        # Aquí dibujaríamos a los personajes y escenarios
        self.jugador.dibujar(self.screen)

        # Dibujar todas las plataformas
        for plataforma in self.plataformas:
            plataforma.dibujar(self.screen)
        #Enemigo
        for enemigo in self.enemigos:
            enemigo.dibujar(self.screen)
        
        #Bala    
        for bala_enemigo in self.balas_enemigo: # <-- DIBUJAR BALAS ENEMIGAS
            bala_enemigo.dibujar(self.screen)
        pygame.display.flip()    
    
    def _load_assets(self):       
        # esto lo hago por que necesito ir una carpeta para atras con el .. y luego entrar al assets
        assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')

        #Cargar las imagenes
        self.assets.load_image('jugador_sprite', os.path.join(assets_dir, 'sprites', 'player.png'))
        self.assets.load_image('enemigo_sprite', os.path.join(assets_dir, 'sprites', 'enemy.png'))
            