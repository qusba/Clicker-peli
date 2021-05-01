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

class TestSaveGame(unittest.TestCase):
    def setUp(self):
        self.gamelogic = GameLogic()
        self.save = SaveGame(self.gamelogic)
    
    def test_saving_works(self):
        self.gamelogic.score = 20
        self.gamelogic.score_per_click = 2
        self.save.savegame()
        self.gamelogic.score = 0
        self.gamelogic.score_per_click = 0
        self.save.loadgame()
        self.assertEqual(self.gamelogic.score,20)
        self.assertEqual(self.gamelogic.score_per_click,2)


    