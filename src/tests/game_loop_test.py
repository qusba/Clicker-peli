
import unittest
import pygame
from game_loop import GameLoop
from ui.colors import Colors
from ui.start_view import StartView
from ui.menu import Menu
from ui.shop import Shop
from event_queue import EventQueue
from game_logic import GameLogic
from repositories.save_game import SaveGame


class StubEvent():
    def __init__(self, type, button, pos):
        self.type = type
        self.button = button
        self.pos = pos


class StubEventQueue():
    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pygame.font.init()
        self.display = pygame.display.set_mode((1024, 640))
        self.gamelogic = GameLogic()
        self.colors = Colors()
        self.startview = StartView(self.display, self.colors)
        self.save = SaveGame(self.gamelogic)
        self.menu = Menu(self.display, self.colors)
        self.shop = Shop(self.display, self.colors, self.gamelogic)
        pygame.init()

    def test_can_close_at_start(self):

        events = [StubEvent(pygame.QUIT, 1, (1024, 0))]
        event_queue = StubEventQueue(events)
        gameloop = GameLoop(self.gamelogic, self.display,
                            self.colors, self.startview, event_queue, self.menu, self.shop, self.save)
        gameloop.start()
        self.assertEqual(gameloop.begin, False)
        self.assertEqual(gameloop.event_handler(), False)

    def test_can_close_after_starting(self):

        events = [StubEvent(pygame.MOUSEBUTTONDOWN, 1, (320, 110)), StubEvent(
            pygame.MOUSEBUTTONDOWN, 1, (320, 110)), StubEvent(pygame.QUIT, 1, (0, 0))]
        event_queue = StubEventQueue(events)
        gameloop = GameLoop(self.gamelogic, self.display,
                            self.colors, self.startview, event_queue, self.menu, self.shop, self.save)
        gameloop.start()
        self.assertEqual(gameloop.begin, False)
        self.assertEqual(gameloop.event_handler(), False)