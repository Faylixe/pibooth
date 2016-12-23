#!/usr/bin/python

from picamera import PiCamera

class Camera(object):
    """ """
    
    def __init__(self):
        """ """
        self.delegate = PiCamera()
    
    def start(self):
        """ """
        self.delegate.start_preview(fullscreen=False, window = (200, 20, 580, 400))

    def stop(self):
        """ """
        self.delegate.stop_preview()