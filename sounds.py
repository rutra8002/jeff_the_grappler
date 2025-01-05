import raylib
import pyray

soundes = {}

def load_sounds():
    raylib.InitAudioDevice()
    soundes["music"] =  pyray.load_music_stream("sounds/testtestmusic.mp3")
    soundes["music"].looping = True
    soundes["level_music"] = pyray.load_music_stream("sounds/testmusic.mp3")
    soundes["level_music"].looping = True