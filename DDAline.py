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

def drawDDA(tx1,ty1,tx2,ty2):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	x,y = tx1,ty1
	length = (tx2-tx1) if (tx2-tx1) > (ty2-ty1) else (ty2-ty1)
	dx = (tx2-tx1)/float(length)
	dy = (ty2-ty1)/float(length)
	
	for i in range(length):
		glBegin(GL_POINTS);
		glVertex2f(x,y);
		glEnd();
		x += dx
		y += dy
	
	glFlush()

x1=int(input("Enter X1 : "))
y1=int(input("Enter Y1 : "))
x2=int(input("Enter X2 : "))
y2=int(input("Enter Y2 : "))
drawDDA(x1,y1,x2,y2)

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
