import json
import os

class SettingsManager:
    def __init__(self, file_path='settings.json'):
        self.file_path = file_path
        self.settings = {
            "fullscreen": False,
            "resolution": (1366, 768),
            "shaders_enabled": False
        }
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.settings = json.load(file)
                self.settings["resolution"] = tuple(self.settings["resolution"])

    def save_settings(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def get_setting(self, key):
        return self.settings.get(key, None)