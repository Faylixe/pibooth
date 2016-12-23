#!/usr/bin/python

from picamera import PiCamera

class Camera(object):
    """ """

    def __init__(self, size=(640, 480)):
        """ """
        self.size = size
        self.delegate = PiCamera()
        self.delegate.image_effect = 'cartoon'
    
    def start(self):
        """ """
        self.delegate.start_preview(fullscreen=False, window = (500, 20, self.size[0] - 500, self.size[1] - 40))

    def stop(self):
        """ """
        self.delegate.stop_preview()