import pygame


class EventQueue():
    """A class for a event queue.

    Mainly used for testing gameloop.
    """
    def get_events(self):
        return pygame.event.get()
