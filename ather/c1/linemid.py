'''
Ather Hussain Malla
Roll no:-12180028
S5
Line by Mid
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
        glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-200,200,-200,200)
	glPointSize(5.0)

def mid(x0,y0,x1,y1):
	dx=x1-x0
	dy=y1-y0
	pk=dy-dx/2
	x=x0
	y=y0
	x=x+1
	while (x<x1):
		x=x+1
		if pk<0:
			pk=pk+dy
		else:
			pk=pk+(dy-dx)
			y=y+1
		glVertex2f(x,y)		
def plotpoint():
        glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
        glPointSize(1.0)
        glBegin(GL_POINTS)
        mid(x0,y0,x1,y1)
	glEnd()
        glFlush()
      
print("Enter x0,y0:")
x0=input()
y0=input()
print("Enter x1,y1:")
x1=input()
y1=input()

def main():
        glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Line by Mid-Point")
	glutDisplayFunc(plotpoint)
        init()
        glutMainLoop()
main()     
           	
