#!/usr/bin/python

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.font.init()

# UI background color.
BACKGROUND_COLOR = (50, 50, 50)

# UI font.
FONT = {
    'small' : pygame.font.Font('resources/fonts/roboto/Roboto-Thin.ttf', 10),
    'medium' : pygame.font.Font('resources/fonts/roboto/Roboto-Thin.ttf', 20),
    'large' : pygame.font.Font('resources/fonts/roboto/Roboto-Thin.ttf', 30),
}

class Clickable(object):
    """ Object that can be clicked. """

    def __init__(self):
        """ Default constructor. """
        self.onClick = None
    

class Container(Clickable):
    """ Base class for graphics object that contains other. """

    def __init__(self):
        """ Default constructor. """
        Clickable.__init__(self)
        self.childs = []

    def add(self, child):
        """ Adds the given child object to this container. """
        self.childs.append(child)
    
    def remove(self, child):
        """ Removes the given child object of this container. """
        if child in self.childs:
            self.childs.remove(child)

    def onClickEvent(self, p):
        """ Handle click event and check if the area of this container has a hit. """
        for child in self.childs:
            if child.bounds is not None:
                b = child.bounds
                if p[0] > b[0] and p[1] > b[1] and p[0] < (b[0] + b[2]) and p[1] < (b[1] + b[3]):
                    if child.onClick is not None:
                        child.onClick()
                    if isinstance(child, Container):
                        child.onClickEvent(p)
                    
class Panel(Container):
    """ Base class for a panel. """
    
    def __init__(self, orientation='vertical', padding=0):
        """ Default constructor. """
        Container.__init__(self)
        self.childs = []
        self.orientation = orientation
        self.padding = padding
        self.bounds = None
    
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
        self.bounds = (position[0], position[1], size[0], size[1])
        return size

class Label(Clickable):
    """ Simple text object. """

    def __init__(self, text, color=(255, 255, 255), size='medium'):
        """ Default constructor. """
        Clickable.__init__(self)    
        self.color = color
        self.font = FONT[size]
        self.text = text
        self.bounds = None
        
    def draw(self, target, position):
        """ Draw the rendered text into the given target at the given position. """
        target.blit(self.font.render(self.text, 1, self.color), position)
        size = self.font.size(self.text)
        self.bounds = (position[0], position[1], size[0], size[1])
        return size

class Image(Clickable):
    """ Simple image object. """

    def __init__(self, path):
        """ Default constructor. """
        Clickable.__init__(self)
        self.delegate = pygame.image.load(path).convert_alpha()
        self.bounds = None

    def draw(self, target, position):
        """ Draw the delegate image into the given target at the given position. """
        target.blit(self.delegate, position)
        size = self.delegate.get_rect()
        self.bounds = (position[0], position[1], size[2], size[3])
        return (size[2], size[3])

class Window(Container):
    """ Window container. """

    def __init__(self, size=(640, 480), backgroundColor=BACKGROUND_COLOR):
        """ Default constructor. """
        Container.__init__(self)
        self.size = size
        self.backgroundColor = backgroundColor
        self.listeners = {}
        self.window = pygame.display.set_mode(size, FULLSCREEN)
        self.running = True
        self.onWindowClick = None

    def invalidate(self):
        """ Invalidates this window and redraws all components for it. """
        self.window.fill(self.backgroundColor)
        for child in self.childs:
            child.draw(self.window, (0, 0))

    def addEventListener(self, key, callback):
        """ """
        self.listeners[key] = callback

    def start(self):
        """ Start this window main loop. """
        self.invalidate()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                   self.onClickEvent(event.pos)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    elif event.key in self.listeners.keys():
                        self.listeners[event.key]()

            pygame.display.flip()

    def onClickEvent(self, p):
        """ """
        if self.onWindowClick is not None:
            self.onWindowClick(p)
        else:
            Container.__onClickEvent(self, p)
            
    def stop(self):
        """ Stop this window. """
        self.running = False