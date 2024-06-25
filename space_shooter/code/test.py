import pygame
from random import randint 
v1 = pygame.math.Vector2(5, 5)
v1.angle_to((-20, 30))
print(v1)

pos = [(randint(0, 600), randint(0, 1000)) for i in range(20)]
print(pos[0][0])