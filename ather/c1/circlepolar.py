'''
Ather Hussain Malla
Roll no:-12180028
S5
Circle by Polar
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)
def bc():
	print("Enter the coordinates of center")
	xc=input()
	yc=input()
	print("Enter the radius")
	r=input()
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	k=math.pi/180
	r,xc,yc=int(r),int(xc),int(yc)
	glBegin(GL_POINTS)
	for angle in range(46):
		x=r*math.cos(k*angle)
		y=r*math.sin(k*angle)
		
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(-x+xc,-y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(y+xc,x+yc)
		glVertex2f(-y+xc,x+yc)
		glVertex2f(-y+xc,-x+yc)
		glVertex2f(y+xc,-x+yc)

	glEnd()
	glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Circle drawing using polar coordinate algorithm")
	glutDisplayFunc(bc)
	init()
	glutMainLoop()
main()
