import pyray
from UI.button import Button

class MapSelectionMenu:
    def __init__(self, width, height, maps):
        self.width = width
        self.height = height
        self.maps = maps
        self.selected_map = None

    def render(self):
        text = "Select Map"
        text_width = pyray.measure_text(text, 40)
        pyray.draw_text(text, int((self.width - text_width) / 2), int(self.height * 0.1), 40, pyray.WHITE)

        columns = 3
        button_width = 200
        button_height = 50
        padding = 10
        start_x = (self.width - (columns * (button_width + padding) - padding)) / 2
        start_y = 200

        for i, map_name in enumerate(self.maps):
            col = i % columns
            row = i // columns
            x = start_x + col * (button_width + padding)
            y = start_y + row * (button_height + padding)
            map_button = Button(x, y, button_width, button_height, map_name, 20, pyray.WHITE, pyray.DARKGRAY,
                                pyray.GRAY, pyray.LIGHTGRAY)
            map_button.update()
            map_button.draw()
            if map_button.is_clicked:
                self.selected_map = map_name
                return "map_selected"

        back_button = Button(self.width / 2 - 100,
                             start_y + (len(self.maps) // columns + 1) * (button_height + padding), 200, 50, "Back",
                             20,
                             pyray.WHITE, pyray.DARKGRAY, pyray.GRAY, pyray.LIGHTGRAY)
        back_button.update()
        back_button.draw()
        if back_button.is_clicked:
            return "back"
        return None