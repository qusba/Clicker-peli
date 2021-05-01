import pygame
from ui.colors import Colors


class StartView():
    """A class responsible of the starting view of the game.

    """
    def __init__(self, display, colors):
        """The constructor of the class.

        Args:
            display: The pygame display in use. Created in the main function.
            colors: The class of colors.
        """
        self.display = display
        self.colors = colors
        self.font = pygame.font.SysFont("Arial", 45)
        self.start_new_game_rect = None
        self.load_game_rect = None

    def view(self):
        """A function responsible of drawing the startview.
        """
        self.display.fill(self.colors.black)
        self.start_new_game_rect = pygame.draw.rect(
            self.display, self.colors.red, (312, 100, 390, 100))
        self.load_game_rect = pygame.draw.rect(
            self.display, self.colors.red, (312, 300, 390, 100))
        start_new_game_text = self.font.render(
            "Start a new game!", True, self.colors.white)
        load_game_text = self.font.render(
            "Load game!", True, self.colors.white)
        self.display.blit(start_new_game_text, (320, 120))
        self.display.blit(load_game_text, (390, 320))
        pygame.display.update()
