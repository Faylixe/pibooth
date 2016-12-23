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
        self.delegate.start_preview(fullscreen=False, window = (200, 20, self.size[0] - 200, self.size[1] - 40))

    def stop(self):
        """ """
        self.delegate.stop_preview()