# -*- coding: utf-8 -*-
# CENG 487 Assignment3 by
# Ekrem Ozturk
# StudentId: 240201006
# 12 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from vec3d import vec3d
from shape import objct
from mat3d import mat3d

from Primitive3D import Primitive3D

class Box:
    
    def __init__(self,quad_length):
        self.primitive3d = self.create_primitive_box(quad_length)
        
        
    def subdivide(self,sud_divide_num):
        self.primitive3d.sub_division_v2(sud_divide_num)
        
        
    def create_primitive_box(self,quadlength):
        initial = mat3d([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]])
        rotation_mat3d = mat3d.rotation_yz_matrix(initial,0.01)

        square1 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(quadlength, quadlength, quadlength, 1.0),	
        	vec3d(quadlength, quadlength, -1*quadlength, 1.0),			
        	vec3d(quadlength, -quadlength, -quadlength, 1.0),
        	vec3d(quadlength, -quadlength, quadlength, 1.0),  
        ], [ # matrix stack
        mat3d.translating_matrix(initial,-1, 1.0, 0.0),
        rotation_mat3d,
       	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        ])

        square2 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(quadlength, quadlength, quadlength, 1.0),	
        	vec3d(-quadlength, quadlength, quadlength, 1.0),			
        	vec3d(-quadlength, -quadlength, quadlength, 1.0),
        	vec3d(quadlength, -quadlength, quadlength, 1.0),			
        
        ], [ # matrix stack
            mat3d.translating_matrix(initial,-1, 1.0, 0.0),
        rotation_mat3d,
           	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        
        ])
        square3 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(quadlength, quadlength, quadlength, 1.0),	
        	vec3d(-quadlength, quadlength, quadlength, 1.0),			
        	vec3d(-quadlength, quadlength, -quadlength, 1.0),
        	vec3d(quadlength, quadlength, -quadlength, 1.0),			
        
        ], [ # matrix stack
            mat3d.translating_matrix(initial,-1, 1.0, 0.0),
        rotation_mat3d,
           	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        
        ])
        
        square4 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(-quadlength, quadlength, quadlength, 1.0),	
        	vec3d(-quadlength, quadlength, -quadlength, 1.0),			
        	vec3d(-quadlength, -quadlength, -quadlength, 1.0),
        	vec3d(-quadlength, -quadlength, quadlength, 1.0),			
        
        ], [ # matrix stack
            mat3d.translating_matrix(initial,-1, 1.0, 0.0),
            rotation_mat3d,
           	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        
        ])
            
        square5 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(-quadlength, -quadlength, -quadlength, 1.0),	
        	vec3d(quadlength, -quadlength, -quadlength, 1.0),			
        	vec3d(quadlength, -quadlength, quadlength, 1.0),
        	vec3d(-quadlength, -quadlength, quadlength, 1.0),			
        
        ], [ # matrix stack
            mat3d.translating_matrix(initial,-1, 1.0, 0.0),
            rotation_mat3d,
           	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        
        ])
        square6 = objct(vec3d(0.0,0.0,0.0, 1.0), # Position
        [ # Vertices
        	vec3d(-quadlength, quadlength, -quadlength, 1.0),	
        	vec3d(quadlength, quadlength, -quadlength, 1.0),			
        	vec3d(quadlength, -quadlength, -quadlength, 1.0),
        	vec3d(-quadlength, -quadlength, -quadlength, 1.0),			
        
        ], [ # matrix stack
            mat3d.translating_matrix(initial,-1, 1.0, 0.0),
        rotation_mat3d,
           	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)
        
        ])            
            
        prim = Primitive3D([square1,square2,square3,square4,square5,square6])
        return prim
    