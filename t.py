from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
def init():
	glClearColor(0.0,0.0,0.0,1.0)    
	gluOrtho2D(-20.0,20.0,-20.0,20.0)
	glPointSize(5.0)

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)

	#draw  point
	glBegin(GL_POINTS)
    	for i in range(-10,10):
    		glVertex2f(i+2.0,0.0)
	glEnd()
	
        
        glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition (50,50)
	glutCreateWindow('Points')
	glutDisplayFunc(plotpoints)
	init()
	glutMainLoop()
main()
