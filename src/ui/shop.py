import pygame
from ui.colors import Colors
from game_logic import GameLogic


class Shop():
    """A class responsible of the shop.
    """
    def __init__(self, display, colors, gamelogic):
        """The constructor of the class.

        Args:
            display: The pygame display in use. Created in the main function.
            colors: The class of colors.
            gamelogic: The class responsible of the games logical functions.
        """
        self.display = display
        self.colors = colors
        self.gamelogic = gamelogic
        self.font = pygame.font.SysFont("Arial", 45)
        self.font2 = pygame.font.SysFont("Arial", 25)

    def open_shop(self):
        """The function responsible of drawing the shop.
        """
        pygame.draw.rect(self.display, self.colors.black, (0, 0, 1024, 640))
        pygame.draw.rect(self.display, self.colors.white, (48, 48, 930, 544))
        pygame.draw.rect(self.display, self.colors.red, (50, 50, 926, 540))

        self.exit_shop_rect = pygame.draw.rect(
            self.display, self.colors.black, (880, 56, 40, 40))
        pygame.draw.line(self.display, self.colors.white,
                         (882, 58), (918, 94), 3)
        pygame.draw.line(self.display, self.colors.white,
                         (918, 58), (882, 94), 3)

        self.click_upgrade_rect = pygame.draw.rect(
            self.display, self.colors.black, (90, 90, 200, 100))
        self.autoclicker_rect = pygame.draw.rect(
            self.display, self.colors.black, (360, 90, 200, 100))
        self.autoclicker_upgrade_rect = pygame.draw.rect(
            self.display, self.colors.black, (630, 90, 200, 100))

        text_click_upgrade_rect = self.font.render(
            "2X", True, self.colors.white)
        text_autoclicker_rect = self.font2.render(
            "Autoclicker", True, self.colors.white)
        text_autoclicker_upgrade_rect2 = self.font2.render(
            "upgrade", True, self.colors.white)

        self.display.blit(text_click_upgrade_rect, (160, 110))
        self.display.blit(text_autoclicker_rect, (400, 120))
        self.display.blit(text_autoclicker_rect, (670, 110))
        self.display.blit(text_autoclicker_upgrade_rect2, (680, 140))

        text_click_upgrade_description1 = self.font2.render(
            "Doubles your", True, self.colors.white)
        text_click_upgrade_description2 = self.font2.render(
            "clicking power!", True, self.colors.white)

        text_autoclicker_description1 = self.font2.render(
            f"Clicks {self.gamelogic.autoclicker_power} times", True, self.colors.white)
        text_autoclicker_description2 = self.font2.render(
            "per second!", True, self.colors.white)

        text_autoclicker_upgrade_description1 = self.font2.render(
            "Doubles your", True, self.colors.white)
        text_autoclicker_upgrade_description2 = self.font2.render(
            "autoclicking power!", True, self.colors.white)

        text_click_upgrade_cost = self.font2.render(
            f"Cost: {self.gamelogic.click_upgrade_cost}", True, self.colors.white)
        text_autoclicker_cost = self.font2.render(
            f"Cost: {self.gamelogic.autoclicker_cost}", True, self.colors.white)
        text_autoclicker_upgrade_cost = self.font2.render(
            f"Cost: {self.gamelogic.autoclicker_upgrade_cost}", True, self.colors.white)
        text_score = self.font2.render(
            "Score: "+str(self.gamelogic.score), True, self.colors.white)

        self.display.blit(text_score, (52, 52))
        self.display.blit(text_click_upgrade_cost, (100, 200))
        self.display.blit(text_autoclicker_cost, (370, 200))
        self.display.blit(text_autoclicker_upgrade_cost, (640, 200))
        self.display.blit(text_click_upgrade_description1, (100, 250))
        self.display.blit(text_click_upgrade_description2, (100, 280))
        self.display.blit(text_autoclicker_description1, (370, 250))
        self.display.blit(text_autoclicker_description2, (370, 280))
        self.display.blit(text_autoclicker_upgrade_description1, (640, 250))
        self.display.blit(text_autoclicker_upgrade_description2, (640, 280))
        pygame.display.update()
