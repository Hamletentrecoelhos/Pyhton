from pygame import *
mixer.init()
mixer.music.load('mp3ar.ogg')
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(10)
