import pyray
import images
import math
import time

class Gun:
    def __init__(self, damage, range, speed, ammo, particle_system, angle=0, cooldown=0.5):
        self.name = self.__class__.__name__
        self.damage = damage
        self.range = range
        self.angle = angle
        self.ammo = ammo
        self.speed = speed
        self.texture = images.textures["deagle"]
        self.particle_system = particle_system
        self.cooldown = cooldown
        self.last_shot_time = 0

    def shoot(self, shooter_x, shooter_y, shooter_width, shooter_height, target_x, target_y):
        current_time = time.time()
        if self.ammo > 0 and (current_time - self.last_shot_time) >= self.cooldown:
            self.ammo -= 1
            self.last_shot_time = current_time

            # Calculate the particle start position outside the shooter
            particle_x = shooter_x + shooter_width // 2
            particle_y = shooter_y + shooter_height // 2

            direction_x = target_x - particle_x
            direction_y = target_y - particle_y
            length = math.sqrt(direction_x ** 2 + direction_y ** 2)
            direction_x /= length
            direction_y /= length

            offset_distance = shooter_width
            particle_x += direction_x * offset_distance
            particle_y += direction_y * offset_distance

            self.particle_system.add_particle(
                particle_x, particle_y, direction_x, direction_y, self.speed, 1, 5, (255, 255, 0, 255), 'circle', self.damage
            )
            return True
        return False

    def reload(self, ammo):
        self.ammo += ammo

    def draw(self, player_x, player_y, player_width, player_height, player_angle, player_vx, camera, target_x,
             target_y):
        angle = math.degrees(math.atan2(target_y - player_y, target_x - player_x))

        source_rect = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest_rect = pyray.Rectangle(player_x, player_y, player_width, player_height)

        if player_vx < 0 and angle == player_angle or angle < -90 or angle > 90:
            source_rect.height = -self.texture.height

        pyray.draw_texture_pro(self.texture, source_rect, dest_rect, pyray.Vector2(player_width / 2, player_height / 2),
                               angle, pyray.WHITE)

class DesertEagle(Gun):
    def __init__(self, damage, range, speed, ammo, particle_system, cooldown=0.5):
        super().__init__(
            damage=damage,
            range=range,
            speed=speed,
            ammo=ammo,
            particle_system=particle_system,
            cooldown=cooldown
        )
        self.texture = images.textures["deagle"]

class Rifle(Gun):
    def __init__(self, damage, range, speed, ammo, particle_system, cooldown=0.1):
        super().__init__(damage, range, speed, ammo, particle_system, cooldown=cooldown)
        self.texture = images.textures["rifle"]

