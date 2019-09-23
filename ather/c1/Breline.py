'''
Ather Hussain Malla
Roll no:-12180028
S5
Line by Bresenham
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def Init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)

def bre(x1,y1,x2,y2):
	mnew=2*(y2-y1)
	sl=mnew-(x2-x1)
	y=y1
  	for x in range(x1,x2+1):
		glVertex2f(x,y)
		sl=sl+mnew
		if(sl>=0):
			y=y+1
			sl=sl-2*(x2-x1)
	
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,22.0,70.0)
	glBegin(GL_POINTS)
	bre(x1,y1,x2,y2)
	glEnd()
	glFlush()

x1=input('\nFirst point x:')
y1=input('\nFirst point y:')
x2=input('\nSecond point x:')
y2=input('\nSecond point y:')
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(1000,1000)
	glutInitWindowPosition(50,50)	
	glutCreateWindow("BRESENHAM'S LINE")
	glutDisplayFunc(plotpoints)
	Init()
	glutMainLoop()
main()

