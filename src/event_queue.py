import pygame

class EventQueue():
    def __init__(self):
        pass

    def get_events(self):
        return pygame.event.get()