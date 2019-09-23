'''
Ather Hussain Malla
Roll no:-12180028
S5
Circle by Mid
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
def midc():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	r,x,y=int(rc),int(xc),int(yc)
	#draw a line
        glBegin(GL_LINES)
        glVertex2i(-200,0)   
        glVertex2i(200,0)
        glVertex2i(0,-200)   
        glVertex2i(0,200)
        glEnd()
	glBegin(GL_POINTS)
	x=0
	y=r
	p=1-r
	#glVertex2f(x,y)
	while(x<y):
		x=x+1
		if(p<0):
			p=p+2*x+1
		else:
			y=y-1
			p=p+2*x-2*y+1

		
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(-x+xc,-y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(y+yc,x+xc)	
		glVertex2f(-y+yc,x+xc)
		glVertex2f(-y+yc,-x+xc)
		glVertex2f(y+yc,-x+xc) 

	glEnd()
	glFlush()
	
print("Enter the coordinates of center")
xc=input()
yc=input()
print("Enter the radius")
rc=input()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Circle drawing using midpoint algorithm")
	glutDisplayFunc(midc)
	init()
	glutMainLoop()
main()
