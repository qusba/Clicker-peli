class GameLogic():
    """A class that is responsible for the games logical functions and important variables.

    """

    def __init__(self):
        """The constructor of the class. Creates all the needed variables.

        """
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
        """Function responsible of producing score.

        """
        self.score += self.score_per_click

    def click_upgrade(self):
        """Function responsible of increasing clicking power.

        Doubles the power of the click() method by
        altering score_per_click variable.
        Increases the cost of the next upgrade.
        """
        if self.score >= self.click_upgrade_cost:
            self.click_upgrades_bought += 1
            self.score_per_click = 2 * self.score_per_click
            self.score -= self.click_upgrade_cost
            self.click_upgrade_cost = 3 * self.click_upgrade_cost

    def autoclicker(self):
        """Function responsible of creating autoclickers.

        Creates an autoclicker for the player and
        increases the cost of the next one.

        """
        if self.score >= self.autoclicker_cost:
            self.autoclickers_bought += 1
            self.score -= self.autoclicker_cost
            self.autoclicker_cost = 3 * self.autoclicker_cost

    def autoclicker_click(self):
        """A function that handles the autoclickers clicking.

        This is called once every second in the gameloop.

        """
        # disabled unused variable error, variable names
        # are needed for the loop to work
        for i in range(self.autoclickers_bought): # pylint: disable=W0612
            for j in range(self.autoclicker_power): # pylint: disable=W0612
                self.click()

    def autoclicker_upgrade(self):
        """A function responsible of upgrading autoclickers.

        Doubles the power of all bought and unbought autoclickers
        and increases the cost of the next upgrade.

        """
        if self.score >= self.autoclicker_upgrade_cost and self.autoclickers_bought > 0:
            self.score -= self.autoclicker_upgrade_cost
            self.autoclicker_upgrades_bought += 1
            self.autoclicker_power = 2 * self.autoclicker_power
            self.autoclicker_upgrade_cost = 3 * self.autoclicker_upgrade_cost
