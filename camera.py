#!/usr/bin/python

from picamera import PiCamera

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
        return self.delegate.IMAGE_EFFECTS

    def setEffect(self, effect):
        """ """
        # TODO : Consider restart.
        if effect in self.effects():
            self.delegate.effect = effect

    def stop(self):
        """ """
        self.delegate.stop_preview()