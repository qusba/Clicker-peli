import pygame
from ui.colors import Colors


class Menu():
    """Class responsible of the menu screen.

    """
    def __init__(self, display, colors):

        """The constructor of the class.

        Args:
            display: The pygame display being used
            colors: The class responsible for colors

        """ 
        self.display = display
        self.colors = colors
        self.font = pygame.font.SysFont("Arial", 45)
        self.font2 = pygame.font.SysFont("Arial", 25)

    def open_menu(self):
        pygame.draw.rect(self.display, self.colors.red, (800, 10, 224, 640))
        self.shop_rect = pygame.draw.rect(
            self.display, self.colors.black, (810, 200, 200, 100))
        self.save_and_exit_rect = pygame.draw.rect(
            self.display, self.colors.black, (810, 400, 200, 100))
        self.exit_menu_rect = pygame.draw.rect(
            self.display, self.colors.black, (980, 20, 40, 40))
        pygame.draw.line(self.display, self.colors.white,
                         (981, 21), (1019, 59), 3)
        pygame.draw.line(self.display, self.colors.white,
                         (1019, 21), (981, 59), 3)

        text_shop = self.font.render("SHOP", True, self.colors.white)
        text_save_and_exit = self.font2.render(
            "SAVE AND EXIT", True, self.colors.white)

        self.display.blit(text_shop, (845, 225))
        self.display.blit(text_save_and_exit, (817, 435))

        pygame.display.update()
