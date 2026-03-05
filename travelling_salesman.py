import pygame
import random
import math

point_amount = 8
background_colour = (255, 255, 255)
(width, height) = (1920, 1080)
MIN_DISTANCE = 150  # Minimum pixels between points

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Travelling Salesman Problem')
screen.fill(background_colour)
pygame.display.flip()

def too_close(new_point, existing_points, min_dist):
    for point in existing_points:
        dx = new_point[0] - point[0]
        dy = new_point[1] - point[1]
        if math.sqrt(dx**2 + dy**2) < min_dist:
            return True
    return False

# Generate random points with minimum spacing
point_list = []
attempts = 0
while len(point_list) < point_amount:
    point_x = random.randint(int(width * 0.25), int(width * 0.75))
    point_y = random.randint(int(height * 0.25), int(height * 0.75))
    candidate = (point_x, point_y)
    if not too_close(candidate, point_list, MIN_DISTANCE):
        point_list.append(candidate)
initual_point = point_list[0]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for centre in point_list:
        pygame.draw.circle(screen, (0, 0, 255), centre, 10)

    pygame.display.flip()

    
