import pickle


class SaveGame():
    """A class responsible of saving and loading the game.

    """

    def __init__(self, gamelogic):
        """Constructor of the class

        Args:
            gamelogic: A class that contains the games logical functions.

        Creates a list for saving variables.
        """
        self.gamelogic = gamelogic
        self.data = 9*[0]

    def savegame(self):
        """A fucntion responsible of saving the game.

        Saves all the important variables of the GameLogic-class into a list. Then uses pickle
        to write that data into a file called save.dat
        """

        self.data[0] = self.gamelogic.score
        self.data[1] = self.gamelogic.click_upgrades_bought
        self.data[2] = self.gamelogic.autoclickers_bought
        self.data[3] = self.gamelogic.autoclicker_upgrades_bought
        self.data[4] = self.gamelogic.score_per_click
        self.data[5] = self.gamelogic.autoclicker_power
        self.data[6] = self.gamelogic.click_upgrade_cost
        self.data[7] = self.gamelogic.autoclicker_cost
        self.data[8] = self.gamelogic.autoclicker_upgrade_cost

        pickle.dump(self.data, open("save.dat", "wb"))

    def loadgame(self):
        """A function responsible of loading the game.
        Rewrites data to be the list saved in save.dat file and then alters variables accordingly.
        """

        self.data = pickle.load(open("save.dat", "rb"))

        self.gamelogic.score = self.data[0]
        self.gamelogic.click_upgrades_bought = self.data[1]
        self.gamelogic.autoclickers_bought = self.data[2]
        self.gamelogic.autoclicker_upgrades_bought = self.data[3]
        self.gamelogic.score_per_click = self.data[4]
        self.gamelogic.autoclicker_power = self.data[5]
        self.gamelogic.click_upgrade_cost = self.data[6]
        self.gamelogic.autoclicker_cost = self.data[7]
        self.gamelogic.autoclicker_upgrade_cost = self.data[8]
