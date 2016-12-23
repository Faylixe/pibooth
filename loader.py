#!/usr/bin/python

from ui import Window, Panel, Label, Image

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Loader(object):
    """ Loader class. """

    def __init__(self, size=(640, 480)):
        """ Default constructor. """
        self.size = size
        self.window = Window(size=size, backgroundColor=WHITE)
        self.container = Panel(orientation='vertical', padding=50)
        self.window.add(self.container)
    
    def welcome(self):
        """ Welcome screen. """
        header = Label('Bienvenue', color=BLACK, size='large')
        message = Label('Appuyer pour commencer', color=BLACK, size='small')
        self.container.add(header)
        self.container.add(message)
        def onClick(position):
            """ """
            self.container.remove(header)
            self.container.remove(message)
            # TODO : Transition to other screen.
        self.window.onWindowClick = onClick

if __name__ == '__main__':
    info = pygame.display.Info()
    size = (info.current_w, info.current_h)
    loader = Loader(size)
    loader.welcome()
    loader.window.start()