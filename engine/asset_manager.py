# /engine/asset_manager.py
import pygame

class AssetManager:
    def __init__(self):        
        self._images = {}
        self._spritesheets = {}

    def load_image(self, name, image_path):
        """
        Carga una imagen 
        """
        try:
            image = pygame.image.load(image_path).convert_alpha()
            self._images[name] = image
        except pygame.error as e:
            print(f"Error al cargar la imagen '{image_path}': {e}")
            self._images[name] = None
    
    def get_image(self, name):
        """
        Devuelve una imagen cargada usando su nombre clave.
        """
        return self._images.get(name)

    def load_spritesheet(self, name, json_path):
        """        
        Carga un spritesheet desde un archivo JSON y su imagen asociada.
        """        
        

    def get_sprite(self, sheet_name, sprite_name):
        """
         Obtiene un sprite individual de un spritesheet cargado.
        """        
        