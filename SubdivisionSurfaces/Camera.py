# -*- coding: utf-8 -*-
# CENG 487 Assignment4 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

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
