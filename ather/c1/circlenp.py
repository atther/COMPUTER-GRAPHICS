'''
Ather Hussain Malla
Roll no:-12180028
S5
Circle by Non Polar
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
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POINTS)
	for i in range(r+1):
		x=i
		y=math.sqrt(r*r-x*x)
		
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

print("Enter the coordinates of center")
xc=input()
yc=input()
print("Enter the radius")
r=input()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Circle drawing using non-polar coordinate algorithm")
	glutDisplayFunc(bc)
	init()
	glutMainLoop()
main()
