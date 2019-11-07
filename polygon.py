from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from DDAline import drawDDA
import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,1.0)    
	gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(5.0)

def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	 
	#draw a line
	glBegin(GL_LINES)
	glVertex2i(-200,0)
	glVertex2i(200,0)
	glVertex2i(0,-200)
	glVertex2i(0,200)
	glEnd()
	glFlush()
	Display1()

def Display1():
	global total_vertex
	for i in range(0,total_vertex):
		drawDDA(x[i],y[i],x[(i+1)%total_vertex],y[(i+1)%total_vertex])


total_vertex=0
x=[]
y=[]
def readinput():
	print("Enter the total number of vertices: ")

	global x, y, total_vertex
	total_vertex = int(input())
	print("Enter the vertices of polygon")
	for i in range(total_vertex):
		print("Enter vertices ",i+1)
		x.append(int(input()))
		y.append(int(input()))
	#print(len(x))

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition (50,50)
	glutCreateWindow('Polygon')
	readinput()
	glutDisplayFunc(plot)
	init()
	glutMainLoop()
if __name__ == "__main__":
	main()

