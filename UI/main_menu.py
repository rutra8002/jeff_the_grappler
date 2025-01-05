import raylib
import sys
import pyray
import os
import shaders
from UI.button import Button
from particles import ParticleSystem
from UI.settings_menu import SettingsMenu
from UI.map_selection_menu import MapSelectionMenu
import random

class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.show_menu = True
        self.show_map_selection = False
        self.show_settings = False
        self.maps = []
        self.selected_map = None
        self.fullscreen = False
        self.resolutions = [(1366, 768), (1920, 1080), (2560, 1440)]
        self.current_resolution_index = 0
        self.start_button = Button(width / 2 - 100, height / 2 - 50, 200, 50, "Start Game", 20, pyray.WHITE,
                                   pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        self.settings_button = Button(width / 2 - 100, height / 2 + 10, 200, 50, "Settings", 20, pyray.WHITE,
                                      pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        self.exit_button = Button(width / 2 - 100, height / 2 + 70, 200, 50, "Exit", 20, pyray.WHITE, pyray.DARKGRAY,
                                  pyray.GRAY, pyray.LIGHTGRAY)
        self.particle_system = ParticleSystem()
        self.settings_menu = SettingsMenu(width, height, self.resolutions, self.current_resolution_index, self.fullscreen)
        self.map_selection_menu = MapSelectionMenu(width, height, self.maps)

    def load_maps(self, directory):
        self.maps = [f for f in os.listdir(directory) if f.endswith('.json')]
        self.map_selection_menu.maps = self.maps

    def render(self):
        pyray.begin_drawing()

        if shaders.shaders_enabled:
            pyray.begin_shader_mode(shaders.shaders["main_menu_background"])

            time_value = pyray.ffi.new("float *", raylib.GetTime())
            raylib.SetShaderValue(shaders.shaders["main_menu_background"],
                                  raylib.GetShaderLocation(shaders.shaders["main_menu_background"], b"time"),
                                  time_value, raylib.SHADER_UNIFORM_FLOAT)

            resolution_value = pyray.ffi.new("float[2]", [self.width, self.height])
            raylib.SetShaderValue(shaders.shaders["main_menu_background"],
                                  raylib.GetShaderLocation(shaders.shaders["main_menu_background"], b"resolution"),
                                  resolution_value, raylib.SHADER_UNIFORM_VEC2)

            pyray.draw_rectangle(0, 0, self.width, self.height, pyray.WHITE)
            pyray.end_shader_mode()
        else:
            pyray.clear_background(pyray.BLACK)
            if random.randint(0, 10) > 8:
                self.particle_system.add_particle(
                    random.uniform(0, self.width),
                    random.uniform(0, self.height),
                    random.uniform(-1, 1),
                    random.uniform(-1, 1),
                    random.randint(10, 50),
                    20,
                    3,
                    (random.randint(1, 150), random.randint(1, 150), random.randint(1, 150), random.randint(50, 200)),
                    'circle',
                    None
                )

        # Update and draw particles
        self.particle_system.update(pyray.get_frame_time(), None, None, None)
        self.particle_system.draw()



        if self.show_menu:
            text = "Main Menu"
            text_width = pyray.measure_text(text, 40)
            pyray.draw_text(text, int((self.width - text_width) / 2), int(self.height * 0.1), 40, pyray.WHITE)

            self.start_button.rect.x = self.width / 2 - self.start_button.rect.width / 2
            self.start_button.rect.y = self.height / 2 - self.start_button.rect.height - 10
            self.start_button.update()
            self.start_button.draw()
            if self.start_button.is_clicked:
                self.show_menu = False
                self.show_map_selection = True

            self.settings_button.rect.x = self.width / 2 - self.settings_button.rect.width / 2
            self.settings_button.rect.y = self.height / 2
            self.settings_button.update()
            self.settings_button.draw()
            if self.settings_button.is_clicked:
                self.show_menu = False
                self.show_settings = True

            self.exit_button.rect.x = self.width / 2 - self.exit_button.rect.width / 2
            self.exit_button.rect.y = self.height / 2 + self.exit_button.rect.height + 10
            self.exit_button.update()
            self.exit_button.draw()
            if self.exit_button.is_clicked:
                pyray.close_window()
                sys.exit()
        elif self.show_map_selection:
            result = self.map_selection_menu.render()
            if result == "map_selected":
                self.selected_map = self.map_selection_menu.selected_map
                self.show_map_selection = False
            elif result == "back":
                self.show_map_selection = False
                self.show_menu = True
        elif self.show_settings:
            result = self.settings_menu.render()
            if result == "back":
                self.show_settings = False
                if self.settings_menu.opened_from_pause_menu:
                    self.settings_menu.opened_from_pause_menu = False
                    self.show_menu = False
                else:
                    self.show_menu = True

        pyray.end_drawing()