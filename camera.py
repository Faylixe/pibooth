#!/usr/bin/python

from picamera import PiCamera

EFFECTS = [
    'Noir et blanc',
    'Avatar',
    'Cartoon',
    'Paint',
    'Sepia',
    'Normal'
]

class Camera(object):
    """ """

    def __init__(self, size=(640, 480)):
        """ """
        self.size = size
        self.delegate = PiCamera()
    
    def start(self):
        """ """
        self.delegate.start_preview(fullscreen=False, window = (500, 20, self.size[0] - 500, self.size[1] - 40))

    def effects(self):
        """ """
        return EFFECTS

    def setEffect(self, effect):
        """ Effect setter."""
        if effect == 'Avatar':
            self.delegate.image_effect = 'colorswap'
        elif effect == 'Cartoon':
            self.delegate.image_effect = 'cartoon'
        elif effect == 'Paint':
            self.delegate.image_effect = 'watercolor'
        elif effect == 'Noir et blanc':
            self.delegate.color_effects = (128, 128)
        elif effect == 'Sepia':
            self.delegate.color_effects = (100, 150)
        else:
            self.delegate.image_effect = 'none'
            self.delegate.color_effects = None


    def stop(self):
        """ """
        self.delegate.stop_preview()