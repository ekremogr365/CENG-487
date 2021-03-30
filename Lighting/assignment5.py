# -*- coding: utf-8 -*-
# CENG 487 Assignment5 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

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
from Light import Light

from ObjParser import *
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
MODE = "NORMAL-SUBDIVISION"

eyeX=0
eyeY=0
eyeZ=35
angle_h = 0.0
angle_v = 0.0
distance = 0.0
drawType = "quads"

prsr = ObjParser("tori.obj")
prsr2 = ObjParser("ecube.obj")
prsr3 = ObjParserTriangleMultiplePrim("cornell.obj")


quad_len = 3
box = Box(quad_len)
sphere = Sphere(5,3,3)
toriShapes = prsr.parse_file()[0]
toriFaces = prsr.parse_file()[1]
toriVertices = prsr.parse_file()[2]

ecubeShapes = prsr2.parse_file()[0]
ecubeFaces = prsr2.parse_file()[1]
ecubeVertices = prsr2.parse_file()[2]

cornellShapes = prsr3.parse_file()

tori = Primitive3D(toriShapes,toriFaces,toriVertices)
ecube = Primitive3D(ecubeShapes,ecubeFaces,ecubeVertices)
tori_for_cage = Primitive3D(toriShapes,toriFaces,toriVertices)
ecube_for_cage = Primitive3D(ecubeShapes,ecubeFaces,ecubeVertices)


print('Argument List:', str(sys.argv))

if len(sys.argv)>1:
    if sys.argv[1]=="cornell.obj":
        SHAPE = "CORNELL"
    elif sys.argv[1]=="tori.obj":
        SHAPE = "T"
    if sys.argv[1]=="ecube.obj":
        SHAPE = "E"
else:
    SHAPE = "CORNELL"


CUBE_DEG_PER_S = 30.0
LIGHT_DEG_PER_S = 90.0
CUBE_SIZE = 9.0


frontLightColor = [ 1, 1, 1 ];
frontLightPos = [ 0, 10, 20, 1.0 ];
frontlight = Light(frontLightPos,10)
topLightColor = [ 1, 1, 1 ];
topLightPos = [ 0, 25, 0, 1.0 ];
produceral_move = "stopped"


# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    global SHAPE
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	

    glEnable(GL_LIGHTING)


    glLightfv(GL_LIGHT1, GL_AMBIENT, topLightColor)
    glLightfv(GL_LIGHT1, GL_POSITION, topLightPos)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0]);
    glLightfv(GL_LIGHT1, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0]);
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [ 0.0, 0.0, -1.0, 0.0]);

    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.0)
    

    glEnable(GL_LIGHT1)



    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(40, float(Width)/float(Height), 0.1, 100.0)

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

    global box,eyeX,eyeY,eyeZ,tori,ecube,cornellShapes,sphere,SHAPE,frontlight,produceral_move, num,number,drawType, time_between_frames, refresh_time,MODE
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
    if(SHAPE=="E"): 
        if(num!=number):
            ecube = Primitive3D(ecubeShapes,ecubeFaces,ecubeVertices)
            if MODE == "CATMULL-CLARK":
                ecube.subdivide_cmc(number)
            if MODE == "NORMAL-SUBDIVISION":
                ecube.sub_division_v2(number)            
            num = number
        scene.drawPrim(ecube,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,drawType)
        if MODE == "CATMULL-CLARK":
            scene.draw_cage(ecube_for_cage)
    if(SHAPE=="T"):  
        if(num!=number):
            tori = Primitive3D(toriShapes,toriFaces,toriVertices)
            if MODE == "CATMULL-CLARK":
                tori.subdivide_cmc(number)
            if MODE == "NORMAL-SUBDIVISION":
                tori.sub_division_v2(number)
            num = number
        scene.drawPrim(tori,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,drawType)
        if MODE == "CATMULL-CLARK":
            scene.draw_cage(tori_for_cage)
    if(SHAPE=="CORNELL"):
        # set up cube's material
        
        
        scene.drawMultiplePrim(cornellShapes,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,drawType)
        if produceral_move == "started":
            pos = frontlight.calculate_new_pos_Y()
        else:
            pos = frontlight.new_pos

        glLightfv(GL_LIGHT0, GL_AMBIENT, frontLightColor);
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0,0,0,1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0]);
        glLightfv(GL_LIGHT0, GL_SPECULAR, [ 1.0, 1.0, 1.0, 1.0]);
        glLightfv(GL_LIGHT0, GL_POSITION, pos)

        glEnable(GL_LIGHT0)

        scene.draw_light_box(pos)
        scene.draw_light_box(topLightPos)


    
    time_after_drawing = time.time()
    if((time_after_drawing-initial_time)<refresh_time):
        time.sleep(refresh_time-(time_after_drawing-initial_time))
    
    glutSwapBuffers()
 
exceed90 = 0
exceedM90 = 0
def specialPressKey(key,x,y):
    global number,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,SHAPE,MOUSEACTIVE,window,exceed90,exceedM90
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
    global number,eyeX,eyeY,eyeZ,angle_h,angle_v,distance,SHAPE,MOUSEACTIVE,window,drawType,MODE,produceral_move
    
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
    if key == 'a'.encode("utf-8"):
        if produceral_move == "stopped":
            produceral_move = "started"
        elif produceral_move == "started":
            produceral_move = "stopped"
    if key == 't'.encode("utf-8"):
        SHAPE = "T"
        number = 1
        glDisable(GL_LIGHTING)
    if key == 'c'.encode("utf-8"):
        SHAPE = "C"
        number = 1
        glDisable(GL_LIGHTING)
    if key == 'e'.encode("utf-8"):
        SHAPE = "E"
        number = 1
        glDisable(GL_LIGHTING)
    if key == 's'.encode("utf-8"):
        SHAPE = "S"
        number = 1
        glDisable(GL_LIGHTING)

    if key == 'm'.encode("utf-8"):
        if MODE == "NORMAL-SUBDIVISION":
            MODE = "CATMULL-CLARK"
        elif MODE == "CATMULL-CLARK":
            MODE = "NORMAL-SUBDIVISION"
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
        print("tori: t\necube: e\ncube: c\nsphere: s")
        print("NEWW!!!! change mode(normal subdivision / catmull clark subdivision(tori and ecube only!!)): m")
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
    window = glutCreateWindow("Ekrem Ozturk Assignment-3")

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