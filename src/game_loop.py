import sys
import pygame


class GameLoop():
    def __init__(self, gamelogic, display, colors, startview):
        self.display = display
        self.gamelogic = gamelogic
        self.colors = colors
        self.startview = startview
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = ""
        self.begin = True

    def start(self):
        if self.begin:
            self.startview.view()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.startview.start_new_game_rect.collidepoint(event.pos):
                            self.begin = False
                            self.start()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.gamelogic.click()
            self.text = self.font.render(
                "Score: "+str(self.gamelogic.score), True, self.colors.red)
            self.display.fill((self.colors.black))
            self.display.blit(self.text, (10, 10))
            pygame.display.update()
            self.clock.tick(60)
