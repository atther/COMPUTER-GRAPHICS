from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from DDAline import drawDDA
import sys
import math
pi=3.14

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
        if case == 1:
            drawDDA(x[i]+tx, y[i]+ty, x[(i + 1) % total_vertex]+tx, y[(i + 1) % total_vertex]+ty)
        if case == 2:
            x1, y1 = map(int, rotation(x[i], y[i]))
            x2, y2 = map(int, rotation(x[(i + 1) % total_vertex], y[(i + 1) % total_vertex]))
            #print("after rotation call  x1 y1 :",x1,y1)
            drawDDA(x1, y1, x2, y2)

        if case==3:
            x1, y1 = map(int, scaling(x[i], y[i]))
            x2, y2 = map(int, scaling(x[(i + 1) % total_vertex], y[(i + 1) % total_vertex]))
            print("after scaling call,  x1 y1 ,x2 ,y2 :", x1, y1, x2 ,y2)
            drawDDA(x1, y1, x2, y2)
def scaling(ex,vi):
    x1 = (ex-xr)*sx + xr
    y1 = (vi-yr)*sy + yr
    return x1,y1

def rotation(ex,vi):
    print(ex,vi)
    x1 = (xr + (ex-xr) * math.cos(theta * pi / 180.0) - (vi-yr) * math.sin(theta * pi / 180.0))
    y1 = (yr + (vi-yr) * math.cos(theta * pi / 180.0) + (ex-xr) * math.sin(theta * pi / 180.0))
    print(x1,y1)
    return x1,y1

def readinput():
    print("Enter the total number of vertices: ")
    global x, y, xr, yr,i, total_vertex
    x = []
    y = []
    xr=0
    yr=0
    total_vertex = int(input())
    print("Enter the vertices of polygon")
    for i in range(total_vertex):
        print("Enter vertices ", i + 1)
        x.append(int(input()))
        y.append(int(input()))

def readtransformation():
    choice = True
    global tx,ty,sx,sy,theta,case
    while(choice == True):
        choice = False
        print("\n1: Translation \n2: Rotation \n3: Scaling")
        case = int(input("Enter your choice : "))
        if case == 1:
            tx,ty=map(int,input("Enter the Translation factor(Delimiter is space) : ").split())
            print(tx,ty)
        elif case == 2:
            theta = int(input("Enter the degree angle to rotate : "))
            print(theta)
        elif case == 3:
            sx,sy=map(float,input("Enter the Scaling factor(Delimiter is space) : ").split())
            print(sx,sy)
        else:
            print("Enter a valid choice!")
            choice=True




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Transformations')
    readinput()
    readtransformation()
    glutDisplayFunc(plot)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
