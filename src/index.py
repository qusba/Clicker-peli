import pygame
from game_logic import GameLogic
from game_loop import GameLoop
from ui.colors import Colors
from ui.start_view import StartView
from event_queue import EventQueue


def main():
    display = pygame.display.set_mode((1024, 640))
    pygame.display.set_caption("Clicker")
    pygame.font.init()
    colors = Colors()
    event_queue = EventQueue()
    startview = StartView(display, colors)
    logic = GameLogic()
    game_loop = GameLoop(logic, display, colors, startview, event_queue)
    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
