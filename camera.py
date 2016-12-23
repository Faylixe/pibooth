#!/usr/bin/python

from picamera import PiCamera

# List of available effects.
EFFECTS = [
    'Normal',
    'Noir et blanc',
    'Sepia',
    'Avatar',
    'Cartoon',
    'Paint'
]

class Camera(object):
    """ Camera processing class. """

    def __init__(self, size=(640, 480)):
        """ Default constructor. """
        self.size = size
        self.delegate = PiCamera()
    
    def start(self):
        """ Starts the camera preview."""
        self.delegate.start_preview(fullscreen=False, window = (350, 10, self.size[0] - 350, self.size[1] - 10))

    def stop(self):
        """ """
        self.delegate.stop_preview()

    def effects(self):
        """  """
        return EFFECTS

    def setEffect(self, effect):
        """ Effect setter."""
        if effect == 'Avatar':
            self.delegate.color_effects = None
            self.delegate.image_effect = 'colorswap'
        elif effect == 'Cartoon':
            self.delegate.color_effects = None
            self.delegate.image_effect = 'cartoon'
        elif effect == 'Paint':
            self.delegate.color_effects = None
            self.delegate.image_effect = 'watercolor'
        elif effect == 'Noir et blanc':
            self.delegate.image_effect = 'none'
            self.delegate.color_effects = (128, 128)
        elif effect == 'Sepia':
            self.delegate.image_effect = 'none'
            self.delegate.color_effects = (100, 150)
        else:
            self.delegate.image_effect = 'none'
            self.delegate.color_effects = None