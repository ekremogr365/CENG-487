# -*- coding: utf-8 -*-
# CENG 487 Assignment# by
# Ekrem Ozturk
# StudentId: 240201006
# November 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import vec3d
from mat3d import mat3d
from shape import objct
import time
import sys


# Number of the glut window.
window = 0

initial = mat3d([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
triangle = objct(vec3d(-2.7, 1, -8.0, 1.0), # Position
[ # Vertices
	vec3d(0.0, 1.0, 0.0, 1.0), 			# Top
	vec3d(1.0, -1.0, 0.0, 1.0),			# Bottom Right
	vec3d(-1.0, -1.0, 0.0, 1.0),		# Bottom Left
],[ # matrix stack
   	mat3d.translating_matrix(initial,-1.0, 1.0, 0.0),
    mat3d.rotation_xy_matrix(initial,0.02),
   	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
]) 
   
square = objct(vec3d(1.1, 1.0, -8.0, 1.0), # Position
[ # Vertices
	vec3d(-1.0, 1.0, 0.0, 1.0),			# Top Left
	vec3d(1.0, 1.0, 0.0, 1.0),			# Top Right
	vec3d(1.0, -1.0, 0.0, 1.0),			# Bottom Right
	vec3d(-1.0, -1.0, 0.0, 1.0)			# Bottom Left
], [ # matrix stack
    mat3d.translating_matrix(initial,-1, 1.0, 0.0),
    mat3d.rotation_xy_matrix(initial,-0.03),
   	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)

])
    
# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    
    
refresh_time = 1/60
time_between_frames=0

def DrawGLScene():
    initial_time= time.time()

    global triangle, square, time_between_frames, refresh_time

    # update shape positions
    triangle.applyMatrixStack()
    square.applyMatrixStack()
    
    # update shape positions
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()					# Reset The View 
    
    glTranslatef(triangle.position.x, triangle.position.y, triangle.position.z)
    
    c1 = vec3d(1.0, 0.0, 0.0, 0.0) 		# Red
    c2 = vec3d(0.0, 1.0, 0.0, 0.0)		# Green
    c3 = vec3d(0.0, 0.0, 1.0, 0.0)		# Blue
    
    # Draw a triangle    
    glBegin(GL_POLYGON)
    glColor3f(c1.x, c1.y, c1.z)
    glVertex3f(triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[0].z)
    glColor3f(c2.x, c2.y, c2.z)
    glVertex3f(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[1].z)
    glColor3f(c3.x, c3.y, c3.z)
    glVertex3f(triangle.vertices[2].x, triangle.vertices[2].y, triangle.vertices[2].z)
    glEnd()
    
    glTranslatef(-triangle.position.x, -triangle.position.y, -triangle.position.z)
    # End of triangle
    
    glTranslatef(square.position.x, square.position.y, square.position.z)
    #Draw a triangle
    glBegin(GL_POLYGON)
    glColor3f(c1.x, c1.y, c1.z)
    glVertex3f(square.vertices[0].x, square.vertices[0].y, square.vertices[0].z)
    glColor3f(c2.x, c2.y, c2.z)
    glVertex3f(square.vertices[1].x, square.vertices[1].y, square.vertices[1].z)
    glColor3f(c3.x, c3.y, c3.z)
    glVertex3f(square.vertices[2].x, square.vertices[2].y, square.vertices[2].z)
    glColor3f(c2.x, c2.y, c2.z)
    glVertex3f(square.vertices[3].x, square.vertices[3].y, square.vertices[3].z)
    glEnd()
    glTranslatef(-square.position.x, -square.position.y, -square.position.z)
    # End of square
    
    time_after_drawing = time.time()
    
    if((time_after_drawing-initial_time)<refresh_time):
        time.sleep(refresh_time-(time_after_drawing-initial_time))
        
    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()
    
    
def keyPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == b'\x1b':
        sys.exit()

def main():
	global window
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	glutInitWindowSize(700, 480)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("Ekrem Ozturk Assignment-1")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc(DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
	
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)

	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)

	# Initialize our window. 
	InitGL(700, 480)

	# Start Event Processing Engine	
	glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
main()