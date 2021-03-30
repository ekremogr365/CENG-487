# -*- coding: utf-8 -*-
# CENG 487 Assignment3 by
# Ekrem Ozturk
# StudentId: 240201006
# 12 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import vec3d
from mat3d import mat3d
from shape import objct
from Primitive3D import Primitive3D
from scene import scene
from Box import Box
from sphere import Sphere

import time
import sys


window = 0

CONSOLEPRINT = 1
MOUSEACTIVE = 0
WIDTH = 700
HEIGHT = 480
refresh_time = 1/40
time_between_frames=0
number = 1
num = 0


eyeX=0
eyeY=0
eyeZ=15
angle_h = 0.0
angle_v = 0.0
distance = 0.0
drawType = "quads"

quad_len = 3
box = Box(quad_len)
sphere = Sphere(5,3,3)

SHAPE = "S"
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
    
    

def DrawGLScene():
    initial_time= time.time()

    global box,eyeX,eyeY,eyeZ,tori,ecube,sphere,SHAPE, num,number,drawType, time_between_frames, refresh_time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()					# Reset The View 

    if(SHAPE=="C"):  
        if(num!=number):
            box = Box(quad_len)
            box.subdivide(number)
            num = number
        scene.drawPrim(box.primitive3d,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,drawType)
    if(SHAPE=="S"): 
        if(num!=number):
            sphere = Sphere(2,2,2)
            sphere = Sphere(2,2+number,2+number)
            num = number
        scene.drawPrim(sphere.primitive3d,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,drawType) 

    scene.draw_xyz_axis()
    
    time_after_drawing = time.time()
    if((time_after_drawing-initial_time)<refresh_time):
        time.sleep(refresh_time-(time_after_drawing-initial_time))
    
    glutSwapBuffers()
 
def specialPressKey(key,x,y):
    global number,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,SHAPE,MOUSEACTIVE,window
    if key == 116:
        MOUSEACTIVE = 1
    if key == GLUT_KEY_LEFT:
        angle_h -=1
    if key == GLUT_KEY_RIGHT:
        angle_h +=1
    if key == GLUT_KEY_UP:
        angle_v +=1
    if key == GLUT_KEY_DOWN:
        angle_v -=1

def specialPressUpKey(key,x,y):
    global number,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,SHAPE,MOUSEACTIVE,window
    if key == 116:
        MOUSEACTIVE = 0


def keyPressed(key, x, y):
    global number,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,SHAPE,MOUSEACTIVE,window,drawType
    
    if key == '+'.encode("utf-8"):
        number = number +1
    if key == '-'.encode("utf-8"):
        if(number!=1):
            number = number -1
    if key == 'q'.encode("utf-8"):
        distance +=0.1
    if key == 'z'.encode("utf-8"):
        distance -=0.1
    if key == 'f'.encode("utf-8"):
        distance = 0
        angle_h = 0
        angle_h = 0
    if key == 'l'.encode("utf-8"):
        if drawType == "lines":
            drawType = "quads"
        else:
            drawType = "lines"
    if key == 'c'.encode("utf-8"):
        SHAPE = "C"
        number = 1
    if key == 's'.encode("utf-8"):
        SHAPE = "S"
        number = 1
    elif key == b'\x1b':
        glutDestroyWindow(windows)
        
lastXPos = WIDTH/2
lastYPos = HEIGHT/2
FIRSTENTER = 1      
MOUSEBUTTON = ""

def keyboard_down(key,x,y):
    global MOUSEACTIVE,FIRSTENTER
    if key ==  b'\t':
        MOUSEACTIVE = 0    
        FIRSTENTER = 1

def mouse(x, y):
    global lastXPos,lastYPos
    if FIRSTENTER ==0:
        lastXPos = x
        lastYPos = y
        
def mouse2(button, state, x, y):
    global MOUSEBUTTON
    if button == GLUT_LEFT_BUTTON:
        MOUSEBUTTON = "left"
    if button == GLUT_RIGHT_BUTTON:
        MOUSEBUTTON = "right"
 
def moveMouse(x,y):
    global angle_h,angle_v,distance,lastXPos,lastYPos,MOUSEBUTTON,MOUSEACTIVE,FIRSTENTER,WIDTH,HEIGHT
    if FIRSTENTER ==1:
        lastXPos = x
        lastYPos = y
        FIRSTENTER = 0
    if MOUSEBUTTON == "left":
        if(MOUSEACTIVE==1):
            x_offset = x - lastXPos
            y_offset = y - lastYPos
            
            angle_h -= x_offset/10
            angle_v += y_offset/10
    if MOUSEBUTTON == "right":  
        if(MOUSEACTIVE==1):
            x_offset = x - lastXPos
            distance -= x_offset/5
    lastXPos = x
    lastYPos = y
      
def main():
    global window,WIDTH,HEIGHT,CONSOLEPRINT
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
    if CONSOLEPRINT == 1:
        print("cube: c\nsphere: s")
        print("camera position change: up-down-right-left arrows/alt+left mouse button")
        print("camera dept change: q-z/alt+right mouse button")
        print("for change view(only edges/full shape): l")
        CONSOLEPRINT = 0
    
    glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	# get a 640 x 480 window 
    glutInitWindowSize(WIDTH, HEIGHT)
	
	# the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
    window = glutCreateWindow("Ekrem Ozturk Assignment-2")

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
    glutKeyboardUpFunc(keyboard_down)
    glutSpecialFunc(specialPressKey)
    glutSpecialUpFunc(specialPressUpKey)

    
    glutMouseFunc(mouse2)
    glutPassiveMotionFunc(mouse)
    glutMotionFunc(moveMouse)

	# Initialize our window. 
    InitGL(700, 480)

	# Start Event Processing Engine	
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
main()