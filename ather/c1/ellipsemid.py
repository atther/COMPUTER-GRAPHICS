'''
Ather Hussain Malla
Roll no:-12180028
S5
Ellipse generation using midpoint algorithm
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

width, height = 500, 500

def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def plot_point():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0, 0.0, 0.0)
	glBegin(GL_POINTS)
	rx = input("enter the radius along x axis\n")
	ry = input("enter the radius along y axis\n")
	xc = input("enter the x coordinate of centre\n")
	yc = input("enter the y coordinate of centre\n")
	x = 0
	y = ry
	glVertex2f(x+xc, y+yc)
	glVertex2f(x+xc, -y+yc)
	glVertex2f(-x+xc, y+yc)
	glVertex2f(-x+xc, -y+yc)
	p1 = ry**2 + 0.25*(rx*rx) - rx*rx*ry
	dx = 2*ry*ry*x
	dy = 2*rx*rx*y
	while( dx < dy):
		if p1 < 0:
			x = x + 1
			dx = dx + (2*ry*ry)
			p1 = p1 + dx + (ry*ry)
		else:
			x = x + 1
			y = y - 1
			dx = dx + (2*ry*ry)
			dy = dy - (2*rx*rx)
			p1 = p1 + dx -dy + (ry*ry)
		glVertex2f(x+xc, y+yc)
		glVertex2f(x+xc, -y+yc)
		glVertex2f(-x+xc, y+yc)
		glVertex2f(-x+xc, -y+yc)
	p2 = ry*ry*(x + 0.5)*(x + 0.5) + rx*rx*(y - 1)*(y - 1) - rx*rx*ry*ry
	while( y >= 0):
		if p2 > 0:
			y = y - 1
			dy = dy - 2*(rx*rx)
			p2 = p2 - dy + rx*rx
		else:
			x = x + 1
			y = y - 1
			dx = dx + (2*ry*ry)
			dy = dy - 2*(rx*rx)
			p2 = p2 + dx - dy + rx+rx
		glVertex2f(x+xc, y+yc)
		glVertex2f(x+xc, -y+yc)
		glVertex2f(-x+xc, y+yc)
		glVertex2f(-x+xc, -y+yc)
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Ellipse_midpoint")
	glutDisplayFunc(plot_point)
	init()
	glutMainLoop()
main()
