# -*- coding: utf-8 -*-
# CENG 487 Assignment3 by
# Ekrem Ozturk
# StudentId: 240201006
# 12 2020

from Box import Box
from vec3d import vec3d
from mat3d import mat3d
import math  

import numpy as np


class Camera:
    
    def __init__(self, look_vec,up_vec,center_position):
        self.look_vec = look_vec
        self.up_vec = up_vec
        self.center_position = center_position
    
    def calculate_right_vec(self):
        lookvec = vec3d(self.center_position.x-self.look_vec.x,self.center_position.y-self.look_vec.y,self.center_position.z-self.look_vec.z,1)
        lookvec_mag = lookvec.calculate_magnitute()
        lookvec = vec3d(lookvec.x/lookvec_mag,lookvec.y/lookvec_mag,lookvec.z/lookvec_mag,1)
        rightvec = vec3d(self.up_vec.x,self.up_vec.y,self.up_vec.z,1).cross_product(lookvec)
        rightvec_mag = rightvec.calculate_magnitute()
        rightvec = vec3d(rightvec.x/rightvec_mag,rightvec.y/rightvec_mag,rightvec.z/rightvec_mag,1)
        return rightvec
    
    def calculate_up_vec(self):
        lookvec = vec3d(self.center_position.x-self.look_vec.x,self.center_position.y-self.look_vec.y,self.center_position.z-self.look_vec.z,1)
        lookvec_mag = lookvec.calculate_magnitute()
        lookvec = vec3d(lookvec.x/lookvec_mag,lookvec.y/lookvec_mag,lookvec.z/lookvec_mag,1)
        rightvec = vec3d(self.up_vec.x,self.up_vec.y,self.up_vec.z,1).cross_product(lookvec)
        rightvec_mag = rightvec.calculate_magnitute()
        rightvec = vec3d(rightvec.x/rightvec_mag,rightvec.y/rightvec_mag,rightvec.z/rightvec_mag,1)
        
        upvec = lookvec.cross_product(rightvec)
        self.up_vec = upvec
        return upvec
                    
    
    def calculate_look_vector_rotate(self,axis, theta):
        axis = np.asarray(axis)
        axis = axis / math.sqrt(np.dot(axis, axis))
        a = math.cos(math.radians(theta / 2.0))
        b, c, d = -axis * math.sin(math.radians(theta / 2.0))
        aa, bb, cc, dd = a * a, b * b, c * c, d * d
        bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
        x = np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                         [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                         [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])
        location =  np.dot(x, [self.look_vec.x,self.look_vec.y,self.look_vec.z])
        location_vec =  vec3d(location[0],location[1],location[2],1)
        self.location_vec = location_vec
        return self.location_vec

    def calculate_look_vector_depth(self,distance):
        look_unit = self.look_vec.calculate_basis_vector()
        x = self.look_vec.x + look_unit.x*distance
        y = self.look_vec.y + look_unit.y*distance
        z = self.look_vec.z + look_unit.z*distance
        new_look_vec = vec3d(x,y,z,1)
        self.location_vec = new_look_vec
        return new_look_vec

"""    

cam = Camera(vec3d(15,0,0,1),vec3d(0,1,0,1),vec3d(0,0,0,1))
x = cam.calculate_look_vector_depth(2)
v = [10, 10, 0]
axis = [0.0, -1, 0]
theta = 75


c = Camera(v)
x = c.rotation_matrix(axis,theta)

print(x.x,x.y,x.z)



def rotation_matrix(axis, theta):

    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(math.radians(theta / 2.0))
    b, c, d = -axis * math.sin(math.radians(theta / 2.0))
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


# [ 2.74911638  4.77180932  1.91629719]


def rotation_matrix(axis, theta):

    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(math.radians(theta / 2.0))
    b, c, d = -axis * math.sin(math.radians(theta / 2.0))
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])





def calculate_locations(vec_center,length,angleZX,angleYZ,angleXY):
    look_vec = vec3d(vec_center.x+length,vec_center.y+length,vec_center.z+length,1)
    
    initial = mat3d([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    mat3dYZ = mat3d.rotation_yz_matrix(initial,angleYZ)
    mat3dZX = mat3d.rotation_zx_matrix(initial,angleZX)
    mat3dXY = mat3d.rotation_xy_matrix(initial,angleXY)
    look_vec = mat3dZX.multiply(look_vec)
    look_vec = mat3dYZ.multiply(look_vec)
    look_vec = mat3dXY.multiply(look_vec)


    return look_vec




def calculate_quaternion(angle,axis_vec):
        unit_axis_vec = axis_vec.calculate_basis_vector()
        
        a = math.cos(math.radians(angle/2))
        b = unit_axis_vec.x*math.sin(math.radians(angle/2))
        c = unit_axis_vec.y*math.sin(math.radians(angle/2))
        d = unit_axis_vec.z*math.sin(math.radians(angle/2))

        quaternion = vec3d(a,b,c,d)
        print(quaternion.x,quaternion.y,quaternion.z,quaternion.w)

        return quaternion

quartenion = calculate_quaternion(50,vec3d(0,2,1,1))
print(math.sin(math.radians(50/2)))

x = quartenion.cross_product(vec3d(10,10,0,1))
print(x.x,x.y,x.z)
x = x.cross_product(vec3d(0.18900063235700051,-0.9063077870366499, -0.0, -0.37800126471400103))

print(x.x,x.y,x.z,x.w)


look_vec = calculate_locations(vec3d(0,0,0,1),30,1,1,1)
eyeX=10
eyeY=10
eyeZ=0
centerX=0
centerY=0.0
centerZ=0
upX=0
upY=0
upZ=0
lookvec = vec3d(centerX-eyeX,centerY-eyeY,centerZ-eyeZ,1)
lookvec_mag = lookvec.calculate_magnitute()
lookvec = vec3d(lookvec.x/lookvec_mag,lookvec.y/lookvec_mag,lookvec.z/lookvec_mag,1)
rightvec = vec3d(0,1,0,1).cross_product(lookvec)
rightvec_mag = rightvec.calculate_magnitute()
rightvec = vec3d(rightvec.x/rightvec_mag,rightvec.y/rightvec_mag,rightvec.z/rightvec_mag,1)

print("rigt",rightvec.x,rightvec.y,rightvec.z)
upvec = lookvec.cross_product(rightvec)
print("rigt",upvec.x,upvec.y,upvec.z)

upX=upvec.x
upY=upvec.y
upZ=upvec.z
"""






