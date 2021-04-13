import pygame
from game_logic import GameLogic
from game_loop import GameLoop





def main():

    display = pygame.display.set_mode((1024,640))
    pygame.display.set_caption("Clicker")
    pygame.font.init()
   

    logic = GameLogic()
    game_loop = GameLoop(logic,display)


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
    


    