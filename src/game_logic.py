class GameLogic():
    def __init__(self):
        self.score = 0
        self.click_upgrades_bought = 0
        self.autoclickers_bought = 0
        self.autoclicker_upgrades_bought = 0
        self.score_per_click = 1
        self.autoclicker_power = 1
        self.click_upgrade_cost = 50
        self.autoclicker_cost = 100
        self.autoclicker_upgrade_cost = 400

    def click(self):
        self.score += self.score_per_click

    def click_upgrade(self):
        if self.score >= self.click_upgrade_cost:
            self.click_upgrades_bought += 1
            self.score_per_click = 2 * self.score_per_click
            self.score -= self.click_upgrade_cost
            self.click_upgrade_cost = 3 * self.click_upgrade_cost

    def autoclicker(self):
        if self.score >= self.autoclicker_cost:
            self.autoclickers_bought += 1
            self.score -= self.autoclicker_cost
            self.autoclicker_cost = 3 * self.autoclicker_cost

    def autoclicker_click(self):
        for i in range(self.autoclickers_bought):
            for j in range(self.autoclicker_power):
                self.click()

    def autoclicker_upgrade(self):
        if self.score >= self.autoclicker_upgrade_cost and self.autoclickers_bought > 0:
            self.score -= self.autoclicker_upgrade_cost
            self.autoclicker_upgrades_bought += 1
            self.autoclicker_power = 2 * self.autoclicker_power
            self.autoclicker_upgrade_cost = 3 * self.autoclicker_upgrade_cost
