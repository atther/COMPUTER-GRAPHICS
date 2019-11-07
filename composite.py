from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from DDAline import drawDDA
import math

pi = 3.14


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)
    glPointSize(5.0)


def plot():
    Display1()
    choice = True
    while choice == True:
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        # draw a line
        glBegin(GL_LINES)
        glVertex2i(-200, 0)
        glVertex2i(200, 0)
        glVertex2i(0, -200)
        glVertex2i(0, 200)
        glEnd()
        readtransformation()
        Display1()
        choice = input("Do you want to transform it again?(y/n) : ")
        if choice == 'y' or choice == 'Y':
            choice = True
        else:
            choice = False


def Display1():
    global total_vertex
    for i in range(0, total_vertex):
        glColor3f(0.0, 0.0, 1.0)
        drawDDA(int(x[i]), int(y[i]), int(x[(i + 1) % total_vertex]), int(y[(i + 1) % total_vertex]))
        glFlush()


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
    global tx, ty, sx, sy, theta, case
    while (choice == True):
        choice = False
        print("\n1: Translation \n2: Rotation \n3: Scaling")
        case = int(input("Enter your choice : "))
        if case == 1:
            tx, ty = map(int, input("Enter the Translation factor(Delimiter is space) : ").split())
            for i in range(total_vertex):
                x[i] += tx
                y[i] += ty
        elif case == 2:
            theta = int(input("Enter the degree angle to rotate : "))
            for i in range(total_vertex):
                ex = x[i]
                x[i] = xr + (x[i] - xr) * math.cos(theta * pi / 180.0) - (y[i] - yr) * math.sin(theta * pi / 180.0)
                y[i] = (yr + (y[i] - yr) * math.cos(theta * pi / 180.0) + (ex - xr) * math.sin(theta * pi / 180.0))

        elif case == 3:
            sx, sy = map(float, input("Enter the Scaling factor(Delimiter is space) : ").split())
            for i in range(total_vertex):
                x[i] = int((x[i] - xr) * sx + xr)
                y[i] = int((y[i] - yr) * sy + yr)
            return int(x[i]), int(y[i])
        else:
            print("Enter a valid choice!")
            choice = True


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Composite Transformations')
    readinput()
    # readtransformation()
    glutDisplayFunc(plot)
    init()
    glutMainLoop()


if __name__ == "__main__":
    main()
