#!/usr/bin/python

from ui import Window, Panel, Label, Image
from camera import Camera

import pygame

from pygame.locals import *

# Constant for booth mode.
PHOTO_MODE = 0
VIDEO_MODE = 1

def onPicturePerformed():
    """ Callback method that handles post picture processing. """
    pass

def onVideoPerformed():
    """ Callback method that handles post video processing. """
    pass

class PiBooth(object):
    """ Main application. """
    
    def __init__(self, camera, size=(640, 480)):
        """ Default constructor. """
        self.inCapture = False
        self.camera = camera
        self.window = Window(size=size)
        self.currentMode = PHOTO_MODE
        self.root = Panel(orientation='horizontal', padding=0)
        self.sidebar = Panel(orientation='vertical')
        self.mode = Panel(orientation='horizontal')
        self.modeLabel = Label('Photo', size='large')
        self.bind()

    def bind(self):
        """ """
        self.sidebar.add(self.mode)
        self.root.add(self.sidebar)
        self.window.add(self.root)

    def createModeController(self):
        """ Creates and configures widget for booth mode controller. """
        photo = Image('resources/icons/photo.png')
        video = Image('resources/icons/video.png')
        self.mode.add(photo)
        self.mode.add(self.modeLabel)
        self.mode.add(video)
        photo.onClick = lambda: self.setMode(PHOTO_MODE)
        video.onClick = lambda: self.setMode(VIDEO_MODE)

    def createSettings(self, effects, callback):
        """ Creates and configures widget for photo configuration. """
        self.sidebar.add(Image('resources/icons/record.png'))
        self.effects = effects
        self.currentEffect = 0
        effectPanel = Panel(orientation='horizontal', padding=0)
        effectPanel.add(Image('resources/icons/filter.png'))
        container = Panel(orientation='horizontal', padding=10)
        prevEffect = Label('<', size='large')
        nextEffect = Label('>', size='large')
        name = Label(self.effects[self.currentEffect], size='large')
        container.add(prevEffect)
        container.add(name)
        container.add(nextEffect)
        effectPanel.add(container)
        self.sidebar.add(effectPanel)

    def setMode(self, mode):
        """ Sets current mode and updates UI accordingly. """
        if self.inCapture or mode == self.currentMode: return
        self.modeLabel.text = 'Photo' if mode == PHOTO_MODE else 'Video'
        self.currentMode = mode
        self.window.invalidate()

    def setEffect(self, iteration):
        """ """
        self.currentEffect += iteration
        if self.currentEffect < 0:
            self.currentEffect = len(self.effects) - 1
        elif self.currentEffect >= len(self.effects):
            self.currentEffect = 0
        self.camera.setEffect(self.effects[self.currentEffect])
        self.window.invalidate()


if __name__ == '__main__':
    info = pygame.display.Info()
    size = (info.current_w, info.current_h)
    camera = Camera(size)
    booth = PiBooth(camera, size=size)
    booth.createModeController()
    booth.createSettings(camera.effects(), lambda effect: camera.setEffect(effect))
    camera.start()
    booth.window.addEventListener(K_LEFT, lambda: booth.setEffect(-1))
    booth.window.addEventListener(K_RIGHT, lambda: booth.setEffect(1))
    booth.window.start()