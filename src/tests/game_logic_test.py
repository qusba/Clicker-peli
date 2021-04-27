import unittest
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.logic = GameLogic()

    def test_clicking_produces_score(self):
        self.logic.click()
        self.assertEqual(self.logic.score, 1)
    
    def test_cannot_purchase_click_upgrade_without_score(self):
        self.logic.score = 30
        self.logic.click_upgrade()
        self.assertEqual(self.logic.score,30)
        self.assertEqual(self.logic.click_upgrades_bought,0)

    def test_can_purchase_click_upgrade_with_sufficent_score(self):
        self.logic.score = 50
        self.logic.click_upgrade()
        self.assertEqual(self.logic.score,0)
        self.assertEqual(self.logic.click_upgrades_bought,1)
    
    def test_click_upgrade_is_working(self):
        self.logic.score = 50
        self.logic.click_upgrade()
        self.assertEqual(self.logic.score_per_click,2)
        self.logic.click()
        self.assertEqual(self.logic.score,2)
        self.logic.score += 148
        self.logic.click_upgrade()
        self.assertEqual(self.logic.score_per_click,4)
        self.logic.click()
        self.assertEqual(self.logic.score,4)



