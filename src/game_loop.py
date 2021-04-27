import pygame


class GameLoop():
    def __init__(self, gamelogic, display, colors, startview, event_queue, menu, shop):
        self.display = display
        self.gamelogic = gamelogic
        self.colors = colors
        self.event_queue = event_queue
        self.startview = startview
        self.menu = menu
        self.shop = shop
        self.clock = pygame.time.Clock()
        self.time_elapsed = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = ""
        self.begin = True
        self.menu_is_open = False
        self.shop_is_open = False

    def start(self):
        while True:

            text_score = self.font.render(
                "Score: "+str(self.gamelogic.score), True, self.colors.white)
            text_menu = self.font.render("Menu", True, self.colors.white)
            self.display.fill((self.colors.black))
            self.menu_rect = pygame.draw.rect(
                self.display, self.colors.red, (900, 10, 120, 70))
            self.display.blit(text_score, (10, 10))
            self.display.blit(text_menu, (930, 28))
            pygame.display.update()

            if self.event_handler() is False:
                break

        pygame.display.quit()
        pygame.quit()

    def event_handler(self):
        tick = self.clock.tick()
        self.time_elapsed += tick
        if self.time_elapsed > 1000:
            self.gamelogic.autoclicker_click()
            self.time_elapsed = 0
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_rect.collidepoint(event.pos):
                    self.menu_is_open = True

                    while self.menu_is_open:
                        self.menu.open_menu()
                        for event in self.event_queue.get_events():
                            if event.type == pygame.QUIT:
                                self.menu_is_open = False
                                return False
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if self.menu.exit_menu_rect.collidepoint(event.pos):
                                    self.menu_is_open = False
                                elif self.menu.shop_rect.collidepoint(event.pos):
                                    self.menu_is_open = False
                                    self.shop_is_open = True
                                elif self.menu.save_and_exit_rect.collidepoint(event.pos):
                                    pass
                    while self.shop_is_open:
                        self.shop.open_shop()
                        for event in self.event_queue.get_events():
                            if event.type == pygame.QUIT:
                                self.shop_is_open = False
                                return False
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if self.shop.exit_shop_rect.collidepoint(event.pos):
                                    self.shop_is_open = False
                                elif self.shop.click_upgrade_rect.collidepoint(event.pos):
                                    self.gamelogic.click_upgrade()
                                elif self.shop.autoclicker_rect.collidepoint(event.pos):
                                    self.gamelogic.autoclicker()
                                elif self.shop.autoclicker_upgrade_rect.collidepoint(event.pos):
                                    self.gamelogic.autoclicker_upgrade()

                else:
                    self.gamelogic.click()
