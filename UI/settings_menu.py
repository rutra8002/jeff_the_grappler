import pyray
import raylib
from UI.button import Button
import shaders

class SettingsMenu:
    def __init__(self, width, height, resolutions, current_resolution_index, fullscreen):
        self.width = width
        self.height = height
        self.resolutions = resolutions
        self.current_resolution_index = current_resolution_index
        self.fullscreen = fullscreen
        self.opened_from_pause_menu = False

    def render(self):
        text = "Settings"
        text_width = pyray.measure_text(text, 40)
        pyray.draw_text(text, int((self.width - text_width) / 2), int(self.height * 0.1), 40, pyray.WHITE)

        shaders_text = "Shaders"
        pyray.draw_text(shaders_text, 50, 215, 20, pyray.WHITE)

        shaders_button_text = "Enabled" if shaders.shaders_enabled else "Disabled"
        shaders_button = Button(200, 200, 200, 50, shaders_button_text, 20,
                                pyray.WHITE, pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        shaders_button.update()
        shaders_button.draw()
        if shaders_button.is_clicked:
            shaders.shaders_enabled = not shaders.shaders_enabled

        resolution_text = "Resolution"
        pyray.draw_text(resolution_text, 50, 275, 20, pyray.WHITE)

        resolution_button_text = f"{self.resolutions[self.current_resolution_index][0]}x{self.resolutions[self.current_resolution_index][1]}"
        resolution_button = Button(200, 260, 200, 50, resolution_button_text, 20,
                                   pyray.WHITE, pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        resolution_button.update()
        resolution_button.draw()
        if resolution_button.is_clicked:
            self.current_resolution_index = (self.current_resolution_index + 1) % len(self.resolutions)
            self.width, self.height = self.resolutions[self.current_resolution_index]
            pyray.set_window_size(self.width, self.height)

        fullscreen_text = "Fullscreen"
        pyray.draw_text(fullscreen_text, 50, 335, 20, pyray.WHITE)

        fullscreen_button_text = "Enabled" if self.fullscreen else "Disabled"
        fullscreen_button = Button(200, 320, 200, 50, fullscreen_button_text, 20,
                                   pyray.WHITE, pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        fullscreen_button.update()
        fullscreen_button.draw()
        if fullscreen_button.is_clicked:
            self.fullscreen = not self.fullscreen
            pyray.toggle_fullscreen()

        back_button = Button(self.width / 2 - 100, self.height / 2 + 70, 200, 50, "Back", 20, pyray.WHITE,
                             pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        back_button.update()
        back_button.draw()
        if back_button.is_clicked:
            return "back"
        return None