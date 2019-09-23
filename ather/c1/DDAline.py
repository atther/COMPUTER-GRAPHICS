'''
Ather Hussain Malla
Roll no:-12180028
S5
Line by dda
'''
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
def init():
	glClearColor(0.0,0.0,0.0,1.0)    
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)

def ROUND(a):
	return int(a + 0.5)

def drawDDA():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	
	for i in range(length):
		glBegin(GL_POINTS);
		glVertex2f(x,y);
		glEnd();
		x += dx
		y += dy
	
	glFlush()

x1=input("Enter X1 : ")
y1=input("Enter Y1 : ")
x2=input("Enter X2 : ")
y2=input("Enter Y2 : ")

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition (50,50)
	glutCreateWindow('Line by DDA')
	glutDisplayFunc(drawDDA)
	init()
	glutMainLoop()
main()
