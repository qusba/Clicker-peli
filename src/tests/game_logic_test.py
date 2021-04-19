import unittest
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pass

    def test_clicking_produces_score(self):
        self.logic = GameLogic()
        self.logic.click()
        self.assertEqual(self.logic.score, 1)
