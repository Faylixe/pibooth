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
mode = Panel(orientation='horizontal')
photo = Image('resources/icons/photo.png')
video = Image('resources/icons/video.png')
label = Label('Photo')

def onPhotoMode():
    print('PHOTO MODE')

def onVideoMode():
    print('VIDEO MODE')

photo.onClick = onPhotoMode
video.onClick = onVideoMode
mode.add(photo)
mode.add(label)
mode.add(video)

# Start button.

# Main panel.
panel = Panel(orientation='vertical', padding=10)
panel.add(mode)
panel.add(Image('resources/icons/record.png'))
# Starting UI thread.
window.add(panel)
window.run()