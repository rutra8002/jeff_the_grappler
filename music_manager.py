import pyray
import sounds

class MusicManager:
    def __init__(self):
        self.current_music = None

    def load_music(self, music_key):
        if music_key in sounds.soundes:
            self.current_music = sounds.soundes[music_key]
        else:
            raise ValueError(f"Music key '{music_key}' not found in sounds.")

    def play_music(self):
        if self.current_music:
            pyray.play_music_stream(self.current_music)
        else:
            raise ValueError("No music loaded to play.")

    def update_music(self):
        if self.current_music:
            pyray.update_music_stream(self.current_music)

    def stop_music(self):
        if self.current_music:
            pyray.stop_music_stream(self.current_music)

    def pause_music(self):
        if self.current_music:
            pyray.pause_music_stream(self.current_music)

    def resume_music(self):
        if self.current_music:
            pyray.resume_music_stream(self.current_music)