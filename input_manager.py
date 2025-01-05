import pyray

class InputManager:
    def __init__(self, dead_zone=0.2):
        self.controller_connected = pyray.is_gamepad_available(0)
        self.dead_zone = dead_zone

    def apply_dead_zone(self, value):
        if abs(value) < self.dead_zone:
            return 0
        return value

    def get_horizontal_input(self):
        if self.controller_connected:
            return self.apply_dead_zone(pyray.get_gamepad_axis_movement(0, pyray.GamepadAxis.GAMEPAD_AXIS_LEFT_X))
        else:
            return int(pyray.is_key_down(pyray.KeyboardKey.KEY_D)) - int(pyray.is_key_down(pyray.KeyboardKey.KEY_A))

    def get_vertical_input(self):
        if self.controller_connected:
            return self.apply_dead_zone(pyray.get_gamepad_axis_movement(0, pyray.GamepadAxis.GAMEPAD_AXIS_LEFT_Y))
        else:
            return int(pyray.is_key_down(pyray.KeyboardKey.KEY_S)) - int(pyray.is_key_down(pyray.KeyboardKey.KEY_W))

    def is_jump_pressed(self):
        if self.controller_connected:
            return pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_DOWN)
        else:
            return pyray.is_key_down(pyray.KeyboardKey.KEY_SPACE)