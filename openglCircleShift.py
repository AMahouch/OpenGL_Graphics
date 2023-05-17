import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Ameen Mahouch
# CSE 3380 - Linear Algebra for CSE
# Dr. Alex Dillhoff

# This code is a simple example of using the Pygame and OpenGL libraries to demonstrate
# a linear transformation of a circle by translating it.
# The circle is initially centered and fills the entire screen.
# In each frame, the circle is translated by (0.01, 0.01) in the x and y directions.


def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def draw_circle(radius=1.0, num_segments=100):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.0)  # Center point of the circle

    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * float(i) / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)

    glEnd()

def main():
    initialize()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslatef(0.01, 0.01, 0.0)  # Translate the circle by (0.01, 0.01)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_circle()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
