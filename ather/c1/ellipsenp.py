'''
Ather Hussain Malla
Roll no:-12180028
S5
Circle by non-polar 
'''



from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
	glPointSize(5.0)
def midc():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POINTS)
	print("Enter the coordinates of center")
	xc=input()
	yc=input()
	print("Enter the radius")
	r=input()
	xc=int(xc)
	yc=int(yc)
	r=int(r)
	for x in range(r+1):
		#x=int(x)
		y=int(math.sqrt(r**2-x**2))
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
	glutCreateWindow("NON POLAR ELLIPSE")
	glutDisplayFunc(midc)
	init()
	glutMainLoop()
main()
