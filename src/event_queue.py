import pygame


class EventQueue():
    def get_events(self):
        return pygame.event.get()
