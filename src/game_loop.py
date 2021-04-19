import sys
import pygame


class GameLoop():
    def __init__(self, gamelogic, display, colors, startview, event_queue):
        self.display = display
        self.gamelogic = gamelogic
        self.colors = colors
        self.event_queue = event_queue
        self.startview = startview
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = ""
        self.begin = True

    def start(self):
        while True:
            if self.event_handler() == False:
                break

            self.text = self.font.render(
                "Score: "+str(self.gamelogic.score), True, self.colors.red)
            self.display.fill((self.colors.black))
            self.display.blit(self.text, (10, 10))
            pygame.display.update()
            self.clock.tick(60)
        pygame.display.quit()
        pygame.quit()

    def event_handler(self):

        while self.begin:
            self.startview.view()
            for event in self.event_queue.get_events():
                if event.type == pygame.QUIT:
                    self.begin = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.startview.start_new_game_rect.collidepoint(event.pos):
                        self.begin = False

        for event in self.event_queue.get_events():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gamelogic.click()
