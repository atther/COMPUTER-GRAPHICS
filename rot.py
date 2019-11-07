from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from DDAline import drawDDA
import sys
import math

pi = 3.14


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)
    glPointSize(5.0)


def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    # draw a line
    glBegin(GL_LINES)
    glVertex2i(-200, 0)
    glVertex2i(200, 0)
    glVertex2i(0, -200)
    glVertex2i(0, 200)
    glEnd()
    glFlush()
    Display1()


def Display1():
    global total_vertex
    for i in range(0, total_vertex):
        glColor3f(1.0, .0, 0.0)
        drawDDA(x[i], y[i], x[(i + 1) % total_vertex], y[(i + 1) % total_vertex])
        glColor3f(0.0, 0.0, 1.0)
        x1, y1 = map(int, rotation(x[i], y[i]))
        x2, y2 = map(int, rotation(x[(i + 1) % total_vertex], y[(i + 1) % total_vertex]))
        drawDDA(x1, y1, x2, y2)






def rotation(ex, vi):
    x1 = (xr + (ex - xr) * math.cos(theta * pi / 180.0) - (vi - yr) * math.sin(theta * pi / 180.0))
    y1 = (yr + (vi - yr) * math.cos(theta * pi / 180.0) + (ex - xr) * math.sin(theta * pi / 180.0))
    return x1, y1


def readinput():
    print("Enter the total number of vertices: ")
    global x, y, xr, yr, i, total_vertex
    x = []
    y = []
    xr = 0
    yr = 0
    total_vertex = int(input())
    print("Enter the vertices of polygon")
    for i in range(total_vertex):
        print("Enter vertices ", i + 1)
        x.append(int(input()))
        y.append(int(input()))


def readtransformation():
    choice = True
    global theta
    theta = int(input("Enter the degree angle to rotate : "))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Transformations:Rotation')
    readinput()
    readtransformation()
    glutDisplayFunc(plot)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
