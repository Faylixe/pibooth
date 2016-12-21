#!/usr/bin/python

import pygame
import pygame.camera

class Camera(object):
    """ """

    def __init__(self, id=None):
        """ """
        if id is None:
            list = pygame.camera.list_cameras()
            self.delegate = pygame.camera.Camera(list[0])            
        else:
            self.delegate = pygame.camera.Camera(id)
    
    