import pygame

""" 
All code comments is in brazilian portuguese, feel free to translate to english if you whant!

"""

class View:
    """ 
        Define uma nova janela, com os seguintes parâmetros:
        bg (RGB colour): a cor da janela
        width (integer): a largura da janela
        height (integer): a altura da janela
        name (string): o nome da janela
    """
    def window(bg, width, height, name):

        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        
        window.fill(bg)
        return window