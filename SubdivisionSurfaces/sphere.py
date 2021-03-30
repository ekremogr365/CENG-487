# -*- coding: utf-8 -*-
# CENG 487 Assignment4 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

from vec3d import vec3d
from shape import objct
from mat3d import mat3d

import math  
from Primitive3D import Primitive3D

class Sphere:
    
    def __init__(self,r,lat,long):
        self.primitive3d = self.create_primitive_sphere(r,lat,long)

        
        
        
    def create_primitive_sphere(self,r,lat,long):
        shapes = []
        for i in range(lat):
            lat0 = math.pi * (-0.5 + (i) / lat)
            for j in range(long+1):
                lng = 2 * math.pi * (j + 1) / long
                quad = self.findQuad(lat0,lng,lat,long,r)
                shapes.append(quad)
        sphere = Primitive3D(shapes)
        return sphere
                
    def findQuad(self,lat_angle,long_angle,lat,long,r):
        vertices = []
        lat_step = math.pi/lat
        long_step = 2 * math.pi/long

        x = (r * math.cos(lat_angle)) * math.cos(long_angle)
        y = (r * math.cos(lat_angle)) * math.sin(long_angle)
        z = r* math.sin(lat_angle)
        vertx1=vec3d(x,y,z,1)
                             
        x = (r * math.cos(lat_angle + lat_step)) * math.cos(long_angle)
        y = (r * math.cos(lat_angle + lat_step)) * math.sin(long_angle)
        z = r* math.sin(lat_angle + lat_step)
        vertx2=vec3d(x,y,z,1)
               
        x = (r * math.cos(lat_angle)) * math.cos(long_angle + long_step)
        y = (r * math.cos(lat_angle)) * math.sin(long_angle + long_step)
        z = r* math.sin(lat_angle)
        vertx3=vec3d(x,y,z,1)
                                   
        x = (r * math.cos(lat_angle + lat_step)) * math.cos(long_angle + long_step)
        y = (r * math.cos(lat_angle + lat_step)) * math.sin(long_angle + long_step)
        z = r* math.sin(lat_angle + lat_step)
        vertx4=vec3d(x,y,z,1)
                 
        vertices.append(vertx4)
        vertices.append(vertx3)
        vertices.append(vertx1)
        vertices.append(vertx2)

        initial = mat3d([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]])
        quad = objct(initial,vertices,[])
        return quad

        
        