'''
Ather Hussain Malla
Roll no:-12180028
S5
Circle by Bresenham
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def Init():
	glClearColor(0.0,0.0,0.0,0.0)    
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)

def bre():
	x=r
	y=0
	p=3-2*r
	while (x>=y):
		y+=1
		if p<0:
			p=p+4*y-6
		else:
			p=p+4*(y-x)+10
			x=x-1
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(-x+xc,-y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(y+yc,x+xc)	
		glVertex2f(-y+yc,x+xc)
		glVertex2f(-y+yc,-x+xc)
		glVertex2f(y+yc,-x+xc)        
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,22.0,70.0)
	#draw a line
        glBegin(GL_LINES)
        glVertex2i(-200,0)   
        glVertex2i(200,0)
        glVertex2i(0,-200)   
        glVertex2i(0,200)
        glEnd()
	glBegin(GL_POINTS)
	bre()
	glEnd()
	glFlush()
xc=input('\nEnter centres x coordinate: ')
yc=input('\nEnter centres y coordinate: ')
r=input('\nEnter the radius of circle: ')

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition (50,50)
	glutCreateWindow('BRSENHAMS CIRCLE')
	glutDisplayFunc(plotpoints)
	Init()
	glutMainLoop()
main()
