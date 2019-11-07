'''
Ather Hussain Malla
Roll no:-12180028
S5
Line by dda
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)
    glPointSize(5.0)



def ROUND(a):
    return int(a + 0.5)


def drawDDA(x1,y1,x2,y2):
    #glClear(GL_COLOR_BUFFER_BIT)
    #glColor3f(0.0, 1.0, 0.0)
    x, y = x1, y1
    steps = abs(x2 - x1) if abs(x2 - x1) > abs(y2-y1) else abs(y2 - y1)
    dx = (x2 - x1) / float(steps)
    dy = (y2 - y1) / float(steps)

    for i in range(steps):
        glBegin(GL_POINTS)
        x += dx
        y += dy
        glVertex2f(x, y)
        glEnd()


    glFlush()
def intake():
    global x1, y1, x2, y2
    x1, y1, x2, y2 = map(int,input("Coordinates : ").split())
    ''' 
    x1 = int(input("Enter X1 : "))
    y1 = int(input("Enter Y1 : "))
    x2 = int(input("Enter X2 : "))
    y2 = int(input("Enter Y2 : "))'''

def disp():
    glClear(GL_COLOR_BUFFER_BIT)
    drawDDA(x1, y1, x2, y2)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Line by DDA')
    intake()
    glutDisplayFunc(disp)
    init()
    glutMainLoop()


if __name__ == "__main__":
	main()