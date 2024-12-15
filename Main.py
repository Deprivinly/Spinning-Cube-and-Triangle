import pygame
from pygame.math import Vector3
import math
import colorsys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Bouncing Color-Changing Cube and 3D Triangle")

# Define cube vertices
vertices = [
    Vector3(-1, -1, -1),
    Vector3(1, -1, -1),
    Vector3(1, 1, -1),
    Vector3(-1, 1, -1),
    Vector3(-1, -1, 1),
    Vector3(1, -1, 1),
    Vector3(1, 1, 1),
    Vector3(-1, 1, 1)
]

# Define cube edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Front face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Back face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Define 3D triangle vertices
triangle_vertices = [
    Vector3(0, 1, 0),     # Top
    Vector3(-1, -1, 1),   # Bottom left front
    Vector3(1, -1, 1),    # Bottom right front
    Vector3(0, -1, -1)    # Bottom back
]

# Define 3D triangle edges
triangle_edges = [
    (0, 1), (1, 2), (2, 0),  # Front face
    (0, 3), (1, 3), (2, 3)   # Connecting to back vertex
]

# Colors
BLACK = (0, 0, 0)

# Rotation variables
angle_x, angle_y, angle_z = 0, 0, 0
rotation_speed = 0.02

# Cube position and velocity
cube_pos = Vector3(width / 3, height / 2, 0)
cube_vel = Vector3(2, 2, 2)

# Triangle position and velocity
triangle_pos = Vector3(2 * width / 3, height / 2, 0)
triangle_vel = Vector3(2, 2, 2)

# Color changing variables
hue = 0
color_speed = 0.005

clock = pygame.time.Clock()

def rotate_point(point, angle_x, angle_y, angle_z):
    # Rotate around X-axis
    y = point.y * math.cos(angle_x) - point.z * math.sin(angle_x)
    z = point.y * math.sin(angle_x) + point.z * math.cos(angle_x)
    point = Vector3(point.x, y, z)

    # Rotate around Y-axis
    x = point.x * math.cos(angle_y) + point.z * math.sin(angle_y)
    z = -point.x * math.sin(angle_y) + point.z * math.cos(angle_y)
    point = Vector3(x, point.y, z)

    # Rotate around Z-axis
    x = point.x * math.cos(angle_z) - point.y * math.sin(angle_z)
    y = point.x * math.sin(angle_z) + point.y * math.cos(angle_z)
    return Vector3(x, y, point.z)

def project_point(point, pos):
    # Increase the factor to make the shapes appear more defined
    factor = 300 / (4 + point.z)
    x = point.x * factor + pos.x
    y = -point.y * factor + pos.y
    return (int(x), int(y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    display.fill(BLACK)

    # Update rotation angles
    angle_x += rotation_speed
    angle_y += rotation_speed
    angle_z += rotation_speed

    # Update cube position
    cube_pos += cube_vel

    # Update triangle position
    triangle_pos += triangle_vel

    # Bounce off walls
    if cube_pos.x < 150 or cube_pos.x > width - 150:
        cube_vel.x *= -1
    if cube_pos.y < 150 or cube_pos.y > height - 150:
        cube_vel.y *= -1

    if triangle_pos.x < 150 or triangle_pos.x > width - 150:
        triangle_vel.x *= -1
    if triangle_pos.y < 150 or triangle_pos.y > height - 150:
        triangle_vel.y *= -1

    # Update color
    hue = (hue + color_speed) % 1.0
    rgb_color = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1)]

    # Rotate and project cube vertices
    rotated_cube_vertices = [rotate_point(v, angle_x, angle_y, angle_z) for v in vertices]
    projected_cube_points = [project_point(v, cube_pos) for v in rotated_cube_vertices]

    # Rotate and project triangle vertices
    rotated_triangle_vertices = [rotate_point(v, angle_x, angle_y, angle_z) for v in triangle_vertices]
    projected_triangle_points = [project_point(v, triangle_pos) for v in rotated_triangle_vertices]

    # Draw cube edges
    for edge in edges:
        start = projected_cube_points[edge[0]]
        end = projected_cube_points[edge[1]]
        pygame.draw.line(display, rgb_color, start, end, 2)

    # Draw triangle edges
    for edge in triangle_edges:
        start = projected_triangle_points[edge[0]]
        end = projected_triangle_points[edge[1]]
        pygame.draw.line(display, rgb_color, start, end, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
