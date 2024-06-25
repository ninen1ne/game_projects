# 17/6/2024
import pygame
from os.path import join
from random import randint




class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.player_direction = pygame.math.Vector2(1, 1)
        self.speed = 500

        # cooldown 
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400


    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        """This method will update player pos."""
        keys = pygame.key.get_pressed()
        self.player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

# define fps
clock = pygame.time.Clock()
FPS = 60
# plain surface
surf = pygame.Surface((100, 200))
surf.fill((173, 216, 153))
x = 100

# create instance of all class and attach it to groups.
all_sprites = pygame.sprite.Group()

star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(20):
    star = Star(all_sprites, star_surf) # create star instance 20 times for random pos to draw

player = Player(all_sprites)



meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = ((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)))

laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()

# custom event => meteor event 
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

# importing an image
running = True
while running:
    dt = clock.tick() / 1000 
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == meteor_event:
        #     print("create meteor")

    # update
    all_sprites.update(dt)

    # draw the game
    display_surface.fill((119, 118, 179))
    all_sprites.draw(display_surface)

    pygame.display.update()
    # can use pygame.display.flip either 
    # but pygame.display.flip can specify what to update but .update will update entire screen.

pygame.quit()