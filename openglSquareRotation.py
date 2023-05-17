import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Ameen Mahouch
# CSE 3380 - Linear Algebra for CSE
# Dr. Alex Dillhoff

# This code uses Pygame and OpenGL to demonstrate a linear
# transformation by rotating a square on the screen.
# The square rotates by 1 degree around the z-axis in each frame.
# The program continuously updates and displays the rotating square.

def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def draw_square():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

def main():
    initialize()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 0, 1)  # Rotate the square by 1 degree around the z-axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
