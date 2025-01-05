import pyray

class InputManager:
    def __init__(self, dead_zone=0.2, mouse_sensitivity=5.0):
        self.controller_connected = pyray.is_gamepad_available(0)
        self.dead_zone = dead_zone
        self.mouse_sensitivity = mouse_sensitivity
        self.left_trigger_pressed = False
        self.right_trigger_pressed = False
        self.left_trigger_state = False
        self.right_trigger_state = False
        self.left_back_pressed = False
        self.right_back_pressed = False
        self.left_back_state = False
        self.right_back_state = False

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

    def get_right_stick_horizontal(self):
        if self.controller_connected:
            return self.apply_dead_zone(pyray.get_gamepad_axis_movement(0, pyray.GamepadAxis.GAMEPAD_AXIS_RIGHT_X))
        return 0

    def get_right_stick_vertical(self):
        if self.controller_connected:
            return self.apply_dead_zone(pyray.get_gamepad_axis_movement(0, pyray.GamepadAxis.GAMEPAD_AXIS_RIGHT_Y))
        return 0

    def update_mouse_position(self):
        if self.controller_connected:
            right_stick_x = self.get_right_stick_horizontal()
            right_stick_y = self.get_right_stick_vertical()
            if right_stick_x != 0 or right_stick_y != 0:
                mouse_position = pyray.get_mouse_position()
                new_mouse_x = mouse_position.x + right_stick_x * self.mouse_sensitivity
                new_mouse_y = mouse_position.y + right_stick_y * self.mouse_sensitivity
                pyray.set_mouse_position(int(new_mouse_x), int(new_mouse_y))

    def is_left_trigger_pressed(self):
        current_state = pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_2)
        if current_state and not self.left_trigger_state:
            self.left_trigger_state = True
            return True
        elif not current_state:
            self.left_trigger_state = False
        return False

    def is_right_trigger_pressed(self):
        current_state = pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_2)
        if current_state and not self.right_trigger_state:
            self.right_trigger_state = True
            return True
        elif not current_state:
            self.right_trigger_state = False
        return False

    def is_left_back_pressed(self):
        current_state = pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_1)
        if current_state and not self.left_back_state:
            self.left_back_state = True
            return True
        elif not current_state:
            self.left_back_state = False
        return False

    def is_right_back_pressed(self):
        current_state = pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_1)
        if current_state and not self.right_back_state:
            self.right_back_state = True
            return True
        elif not current_state:
            self.right_back_state = False
        return False

    def is_slide_pressed(self):
        return self.controller_connected and pyray.is_gamepad_button_down(0, pyray.GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_LEFT)