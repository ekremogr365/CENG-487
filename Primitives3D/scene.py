# -*- coding: utf-8 -*-
# CENG 487 Assignment3 by
# Ekrem Ozturk
# StudentId: 240201006
# 12 2020

from Box import Box
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import vec3d
from mat3d import mat3d
from Camera import Camera
from ObjParser import ObjParser
from Primitive3D import Primitive3D

import math  
tempx=0.0
tempz=0.0
tempy=0.0
eyeX=15.0
eyeY= 0.0
eyeZ= 0.0
upX=0.0
upY=1.0
upZ=0.0

class scene:
    
    def __init__(self, shapes):
        self.shapes = shapes
        
        
    def drawBox(box,x,y,z,angle_h,angle_v,distanca):
        global tempx,tempz,tempy,eyeX,eyeY,eyeZ,upX,upY,upZ
        cam = Camera(vec3d(15,0,0,1),vec3d(0,1,0,1),vec3d(0,0,0,1))

        c1 = vec3d(1.0, 0.0, 0.0, 0.0) 		# Red
        c2 = vec3d(0.0, 1.0, 0.0, 0.0)		# Green
        c3 = vec3d(0.0, 0.0, 1.0, 0.0)		# Blue
        
        #for shape in box.primitive3d.shapes:
         #   shape.applyMatrixStack()
        upvec = cam.calculate_up_vec()
        axis = [upvec.x, upvec.y, upvec.z]  
        r = cam.calculate_right_vec()
        lool_vec = cam.calculate_look_vector_rotate(axis,angle_h)
        eyeX = lool_vec.x
        eyeY = lool_vec.y
        eyeZ = lool_vec.z
        
        cam = Camera(vec3d(eyeX,eyeY,eyeZ,1),vec3d(upvec.x,upvec.y,upvec.z,1),vec3d(0,0,0,1))
        r = cam.calculate_right_vec()
        axis2 = [r.x, r.y, r.z]        
        lool_vec2 = cam.calculate_look_vector_rotate(axis2,angle_v)
        eyeX = lool_vec2.x
        eyeY = lool_vec2.y
        eyeZ = lool_vec2.z
        
        cam = Camera(vec3d(eyeX,eyeY,eyeZ,1),vec3d(upvec.x,upvec.y,upvec.z,1),vec3d(0,0,0,1))
        look_vec = cam.calculate_look_vector_depth(distanca)
        eyeX = look_vec.x
        eyeY = look_vec.y
        eyeZ = look_vec.z
        
        upvec = cam.calculate_up_vec()
        
        gluLookAt(eyeX,eyeY,eyeZ,0,0,0,upvec.x,upvec.y,upvec.z)
        
        
        s = Sphere(3,10,10)
        ver = s.create_primitive_sphere()
        glBegin(GL_QUADS)

        for v in ver:
            glColor3f(c1.x, c1.y, c1.z)
            glVertex3f(v[0].x, v[0].y, v[0].z)
            glColor3f(c2.x, c2.y, c2.z)
            glVertex3f(v[1].x, v[1].y, v[1].z)
            glColor3f(c3.x, c3.y, c3.z)
            glVertex3f(v[2].x, v[2].y, v[2].z)
            glColor3f(c2.x, c2.y, c2.z)
            glVertex3f(v[3].x, v[3].y, v[3].z)
        glEnd()
        
        glBegin(GL_QUADS)

        
        for shape in box.primitive3d.shapes:
            glColor3f(c1.x, c1.y, c1.z)
            glVertex3f(shape.vertices[0].x, shape.vertices[0].y, shape.vertices[0].z)
            glColor3f(c2.x, c2.y, c2.z)
            glVertex3f(shape.vertices[1].x, shape.vertices[1].y, shape.vertices[1].z)
            glColor3f(c3.x, c3.y, c3.z)
            glVertex3f(shape.vertices[2].x, shape.vertices[2].y, shape.vertices[2].z)
            glColor3f(c2.x, c2.y, c2.z)
            glVertex3f(shape.vertices[3].x, shape.vertices[3].y, shape.vertices[3].z)
        glEnd()
        
    def drawPrim(primitive,x,y,z,angle_h,angle_v,distanca,drawType):
        global tempx,tempz,tempy,eyeX,eyeY,eyeZ,upX,upY,upZ
        cam = Camera(vec3d(15.0,0.0,0.0,1.0),vec3d(0.0,1.0,0.0,1.0),vec3d(0.0,0.0,0.0,1.0))

        c1 = vec3d(1.0, 0.0, 0.0, 0.0) 		# Red
        c2 = vec3d(0.0, 1.0, 0.0, 0.0)		# Green
        c3 = vec3d(0.0, 0.0, 1.0, 0.0)		# Blue
        
        #for shape in box.primitive3d.shapes:
         #   shape.applyMatrixStack()
        upvec = cam.calculate_up_vec()
        axis = [upvec.x, upvec.y, upvec.z]  
        r = cam.calculate_right_vec()
        axis2 = [r.x, r.y, r.z]   
        lool_vec = cam.calculate_look_vector_rotate(axis,angle_h)
        eyeX = lool_vec.x
        eyeY = lool_vec.y
        eyeZ = lool_vec.z
        tempx = angle_h
        
        cam = Camera(vec3d(eyeX,eyeY,eyeZ,1),vec3d(upvec.x,upvec.y,upvec.z,1),vec3d(0.0,0.0,0.0,1.0))
        r = cam.calculate_right_vec()
        axis2 = [r.x, r.y, r.z]        
        lool_vec2 = cam.calculate_look_vector_rotate(axis2,angle_v)
        eyeX = lool_vec2.x
        eyeY = lool_vec2.y
        eyeZ = lool_vec2.z
        tempz=angle_v
        
        cam = Camera(vec3d(eyeX,eyeY,eyeZ,1),vec3d(upvec.x,upvec.y,upvec.z,1),vec3d(0.0,0.0,0.0,1.0))
        look_vec = cam.calculate_look_vector_depth(distanca)
        eyeX = look_vec.x
        eyeY = look_vec.y
        eyeZ = look_vec.z
        tempy=distanca
        
        upvec = cam.calculate_up_vec()

        gluLookAt(eyeX,eyeY,eyeZ,0.0,0.0,0.0,upvec.x,upvec.y,upvec.z)
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
        if(drawType=="lines"):
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
            glBegin(GL_QUADS)
            glColor3f(1,1,1)

            for shape in primitive.shapes:
                glVertex3f(shape.vertices[0].x, shape.vertices[0].y, shape.vertices[0].z)
                glVertex3f(shape.vertices[1].x, shape.vertices[1].y, shape.vertices[1].z)
                glVertex3f(shape.vertices[2].x, shape.vertices[2].y, shape.vertices[2].z)
                glVertex3f(shape.vertices[3].x, shape.vertices[3].y, shape.vertices[3].z)
            glEnd()
        else:
            glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

            glBegin(GL_QUADS)
    
            for shape in primitive.shapes:
                glColor3f(shape.color.x,shape.color.y,shape.color.z)
                glVertex3f(shape.vertices[0].x, shape.vertices[0].y, shape.vertices[0].z)
                glVertex3f(shape.vertices[1].x, shape.vertices[1].y, shape.vertices[1].z)
                glVertex3f(shape.vertices[2].x, shape.vertices[2].y, shape.vertices[2].z)
                glVertex3f(shape.vertices[3].x, shape.vertices[3].y, shape.vertices[3].z)
            glEnd()
        
        
    def draw_xyz_axis():
        glPushMatrix();

        glBegin(GL_LINES);
    
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(50.0, 0.0, 0.0);
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(-50.0, 0.0, 0.0);
    
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, 50.0, 0.0);
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, -50.0, 0.0);
        
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, 0.0, 50.0);
        glColor3f (1.0, 1.0, 1.0);
        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, 0.0, -50.0);
        glEnd();
    
        glPopMatrix();
        
        
    
"""
quad_len = 3
box = Box(quad_len)
scene.drawBox(box,1,1,1,2,2,2)    
"""