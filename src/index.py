import pygame
from game_logic import GameLogic
from game_loop import GameLoop
from ui.colors import Colors
from ui.start_view import StartView
from ui.menu import Menu
from ui.shop import Shop
from event_queue import EventQueue
from repositories.save_game import SaveGame


def main():
    display = pygame.display.set_mode((1024, 640))
    pygame.display.set_caption("Clicker")
    pygame.font.init()
    colors = Colors()
    event_queue = EventQueue()
    startview = StartView(display, colors)
    menu = Menu(display, colors)
    logic = GameLogic()
    shop = Shop(display, colors, logic)
    save = SaveGame(logic)
    game_loop = GameLoop(logic, display, colors,
                         startview, event_queue, menu, shop, save)
    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
