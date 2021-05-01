import pygame


class GameLoop():
    """The class that keeps the game running
    """

    def __init__(self, gamelogic, display, colors, startview, event_queue, menu, shop, save):
        """The constructor of the class.

        Args:
            gamelogic: A class that contains the games logical functions.
            display: The pygame display being used.
            colors: A class that has all the colors being used.
            startview: A class that draws the starting screen.
            event_queue: A queue of pygame events, mainly for testing.
            menu: A class that draws the menu.
            shop: A class that draws the shop.
            save: A class that handles saving and loading the game.
            clock: Creates a clock for pygame.
            time_elapsed: A variable used to determine automatic functions.
            font: A pygame font for drawing text.
            begin: A boolean value to determine whether the starting screen should be on or off.
            menu_is_open: Same purpose as begin for menu.
            shop_is_open: Same puerpose as begin for shop.
        """
        self.display = display
        self.gamelogic = gamelogic
        self.colors = colors
        self.event_queue = event_queue
        self.startview = startview
        self.gamesaver = save
        self.menu = menu
        self.shop = shop
        self.clock = pygame.time.Clock()
        self.time_elapsed = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = ""
        self.begin = True
        self.click_rect = None
        self.menu_rect = None
        self.menu_is_open = False
        self.shop_is_open = False

    def start(self):
        """The Function responsible of running the game.
         Also draws the "main" screen.
        """
        while True:

            text_score = self.font.render(
                "Score: "+str(self.gamelogic.score), True, self.colors.white)
            text_menu = self.font.render("Menu", True, self.colors.white)
            self.display.fill((self.colors.black))
            self.menu_rect = pygame.draw.rect(
                self.display, self.colors.red, (900, 10, 120, 70))
            self.click_rect = pygame.draw.circle(
                self.display, self.colors.red, (512, 320), 150)
            self.display.blit(text_score, (10, 10))
            self.display.blit(text_menu, (930, 28))
            pygame.display.update()

            if self.event_handler() is False:
                break

        pygame.display.quit()
        pygame.quit()

    def event_handler(self):
        """ A function responsible of handling pygame events.

        Handles all the players clicking actions as well as autoclickers and responds accordingly.

        Returns:
            False: ends the main loop of the game
        """
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
                    elif self.startview.load_game_rect.collidepoint(event.pos):
                        self.gamesaver.loadgame()
                        self.begin = False

        for event in self.event_queue.get_events():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_rect.collidepoint(event.pos):
                    self.menu_is_open = True

                    while self.menu_is_open:
                        self.menu.open_menu()
                        for event2 in self.event_queue.get_events():
                            if event2.type == pygame.QUIT:
                                self.menu_is_open = False
                                return False
                            if event2.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if self.menu.exit_menu_rect.collidepoint(event.pos):
                                    self.menu_is_open = False
                                elif self.menu.shop_rect.collidepoint(event.pos):
                                    self.menu_is_open = False
                                    self.shop_is_open = True
                                elif self.menu.save_and_exit_rect.collidepoint(event.pos):
                                    self.gamesaver.savegame()
                                    return False
                    while self.shop_is_open:
                        self.shop.open_shop()
                        for event3 in self.event_queue.get_events():
                            if event3.type == pygame.QUIT:
                                self.shop_is_open = False
                                return False
                            if event3.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if self.shop.exit_shop_rect.collidepoint(event.pos):
                                    self.shop_is_open = False
                                elif self.shop.click_upgrade_rect.collidepoint(event.pos):
                                    self.gamelogic.click_upgrade()
                                elif self.shop.autoclicker_rect.collidepoint(event.pos):
                                    self.gamelogic.autoclicker()
                                elif self.shop.autoclicker_upgrade_rect.collidepoint(event.pos):
                                    self.gamelogic.autoclicker_upgrade()

                elif self.click_rect.collidepoint(event.pos):
                    self.gamelogic.click()
