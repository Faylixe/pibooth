#!/usr/bin/python

from ui import Window, Panel, Label, Image

def onPicturePerformed():
    """ Callback method that handles post picture processing. """
    pass

def onVideoPerformed():
    """ Callback method that handles post video processing. """
    pass

# Top container.
window = Window()

# Photo / Video switch.
icons = Panel(orientation='horizontal')
icons.add(Image('resources/icons/photo.png'))
icons.add(Image('resources/icons/video.png'))

# Photo / Video label.
label = Panel(orientation='horizontal')
label.add(Label('Photo'))

# Main panel.
panel = Panel(orientation='vertical')
panel.add(icons)
panel.add(label)

# Starting UI thread.
window.add(panel)
window.run()