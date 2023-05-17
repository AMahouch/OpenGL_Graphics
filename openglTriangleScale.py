import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

# Ameen Mahouch
# CSE 3380 - Linear Algebra for CSE
# Dr. Alex Dillhoff

# This code is a simple example of using the Pygame and OpenGL libraries to
# apply a linear transformation to a triangle on the screen by scaling it.

# The triangle is initially centered and fills the entire screen.
# In each frame, the triangle is scaled down by 1% in both the x and y directions.
# The program continuously updates and displays the scaling triangle.


def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
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

        glScalef(0.99, 0.99, 1.0)  # Scale the triangle down by 1% in both x and y directions

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
