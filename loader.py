#!/usr/bin/python

from ui import Window, Panel, Label, Image

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

class Loader(object):
    """ Loader class. """

    def __init__(self, size=(640, 480)):
        """ Default constructor. """
        self.size = size
        self.window = Window(size=size, fullscreen=False, backgroundColor=WHITE)
        self.container = Panel(orientation='vertical')
        self.window.add(self.container)
    
    def welcome(self):
        """ Welcome screen. """
        header = Label('Bienvenue', color=BLACK, size='huge')
        message = Label('Appuyer pour commencer', color=BLACK, size='medium')
        self.container.add(header)
        self.container.add(message)
        def onClick(position):
            """ Window click callback. """
            self.container.remove(header)
            self.container.remove(message)
            self.window.onWindowClick = None
            self.prompt('Voulez vous configurer la connection internet ?', lambda r: self.wifi(r))
        self.window.onWindowClick = onClick

    def prompt(self, question, callback):
        """ Prompt screen (Yes / No question only) """
        header = Label(question, color=BLACK, size='medium')
        panel = Panel(orientation='horizontal', padding=20)
        def createPromptCallback(callback, answer):
            def delegate():
                self.container.remove(header)
                self.container.remove(panel)
                callback(answer)
            return delegate
        yes = Label(' Oui ', color=WHITE, background=GRAY, size='medium')
        no = Label(' Non ', color=WHITE, background=GRAY, size='medium')
        yes.onClick = createPromptCallback(callback, True)
        no.onClick = createPromptCallback(callback, False)
        panel.add(yes)
        panel.add(no)
        self.container.add(header)
        self.container.add(panel)
        self.window.invalidate()

    def wifi(self, configure):
        """ WiFi configuration screen. """
        if configure:
            # TODO : Set RPI as WiFi hotspot.
            # TODO : Start webserver.
            # TODO : Quit and go next.
            pass
        else:
            quit()

if __name__ == '__main__':
    info = pygame.display.Info()
    loader = Loader()
    loader.welcome()
    loader.window.start()