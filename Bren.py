from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
def init():
	glClearColor(0.0,0.0,0.0,1.0)    
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)

def drawPixel(x, y): 
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
	
	
def drawLine():
	
	dx = x2-x1;
	dy = y2-y1;

	if (dx < 0):
		dx = -dx;
	if (dy < 0):
		dy = -dy;
	incx = 1;
	if (x2 < x1):
		incx = -1;
	incy = 1;
	if (y2 < y1):
		incy = -1;
	x = x1; y = y1;
	if (dx > dy):
		drawPixel(x, y);
		e = 2*dy-dx;
		inc1 = 2*(dy-dx);
		inc2 = 2*dy;
		for i in range(dx):
			if (e >= 0): 
				y += incy;
				e += inc1;
			else:
				e += inc2;
			x += incx;
			drawPixel(x,y);
	else:
		drawPixel(x, y);
		e = 2*dx-dy;
		inc1 = 2*(dx-dy);
		inc2 = 2*dx;
		for i in range(dy):
			if (e >= 0): 
				x += incx;
				e += inc1;
			
			else:
				e += inc2;
			y += incy;
			drawPixel(x, y);

def myDisplay():
	drawLine();
	glFlush();	
	

x1=input("Enter X1 : ")
y1=input("Enter Y1 : ")
x2=input("Enter X2 : ")
y2=input("Enter Y2 : ")

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition (50,50)
	glutCreateWindow('Line by BRESENHAM')
	glutDisplayFunc(myDisplay)
	init()
	glutMainLoop()
main()
