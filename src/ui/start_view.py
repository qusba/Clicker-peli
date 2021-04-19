import pygame
from ui.colors import Colors


class StartView():
    def __init__(self, display, colors):
        self.display = display
        self.colors = colors
        self.font = pygame.font.SysFont("Arial", 45)
        self.start_new_game_rect = None
        self.load_game_rect = None

    def view(self):
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
