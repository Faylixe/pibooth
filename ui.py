#!/usr/bin/python

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.font.init()

# UI background color.
BACKGROUND_COLOR = (50, 50, 50)

# UI font.
FONT = pygame.font.Font('resources/fonts/roboto/Roboto-Thin.ttf', 30) # TODO : Configure

class Container(object):
    """ Base class for graphics object that contains other. """

    def __init__(self):
        """ Default constructor. """
        self.childs = []

    def add(self, child):
        """ Adds the given child object to this container. """
        self.childs.append(child)

class Panel(Container):
    """ Base class for a panel. """
    
    def __init__(self, orientation='vertical', padding=20):
        """ Default constructor. """
        Container.__init__(self)
        self.childs = []
        self.orientation = orientation
        self.padding = padding
    
    def draw(self, target, position):
        """ Draw this panel content. """
        # TODO : Consider drawing panel itself ?
        offset = self.padding
        size = [self.padding * 2, self.padding * 2]
        for child in self.childs:
            childPosition = [position[0], position[1]]
            childPosition[0 if self.orientation == 'horizontal' else 1] += offset
            childPosition[1 if self.orientation == 'horizontal' else 0] += self.padding
            childSize = child.draw(target, childPosition)
            offset += self.padding
            offset += childSize[0] if self.orientation == 'horizontal' else childSize[1]
            size[0] = (size[0] + childSize[0] + self.padding) if self.orientation == 'horizontal' else max(childSize[0], size[0])
            size[1] = (size[1] + childSize[1] + self.padding) if self.orientation == 'vertical' else max(childSize[1], size[1])
        return size

class Label(object):
    """ Simple text object. """

    def __init__(self, text, color=(255, 255, 255), font=FONT):
        """ Default constructor. """
        self.color = color
        self.font = font
        self.text = text
        
    def draw(self, target, position):
        """ Draw the rendered text into the given target at the given position. """
        target.blit(self.font.render(self.text, 1, self.color), position)
        return self.font.size(self.text)

class Image(object):
    """ Simple image object. """

    def __init__(self, path):
        """ Default constructor. """
        self.delegate = pygame.image.load(path).convert_alpha()

    def draw(self, target, position):
        """ Draw the delegate image into the given target at the given position. """
        target.blit(self.delegate, position)
        size = self.delegate.get_rect()
        return (size[2], size[3])

class Window(Container):
    """ Window container. """

    def __init__(self, size=(640, 480)):
        """ Default constructor. """
        Container.__init__(self)
        self.size = size
        self.window = pygame.display.set_mode(size)
        self.running = True

    def invalidate(self):
        """ """
        self.window.fill(BACKGROUND_COLOR)
        for child in self.childs:
            child.draw(self.window, (0, 0))

    def run(self):
        """ """
        # TODO : Consider running this in a single thread.
        self.invalidate()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.flip()
