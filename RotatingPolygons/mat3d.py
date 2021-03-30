# -*- coding: utf-8 -*-
# CENG 487 Assignment# by
# Ekrem Ozturk
# StudentId: 240201006
# November 2020

import copy
import math  
from vec3d import vec3d


class mat3d :
    def __init__(self, matrix):
        self.matrix = matrix
        
        
    def multiply(self,vec3dd):
        return vec3d(
            vec3d(self.matrix[0][0],self.matrix[0][1],self.matrix[0][2],self.matrix[0][3]).dot_product(vec3dd), 
            vec3d(self.matrix[1][0],self.matrix[1][1],self.matrix[1][2],self.matrix[1][3]).dot_product(vec3dd), 
            vec3d(self.matrix[2][0],self.matrix[2][1],self.matrix[2][2],self.matrix[2][3]).dot_product(vec3dd), 
            vec3d(self.matrix[3][0],self.matrix[3][1],self.matrix[3][2],self.matrix[3][3]).dot_product(vec3dd))
        
        
    def scaling_matrix(self,scale_x,scale_y,scale_z):
        self.matrix[0][0] = self.matrix[0][0]*scale_x
        self.matrix[1][1] = self.matrix[1][1]*scale_y
        self.matrix[2][2] = self.matrix[2][2]*scale_z
        return self.matrix
    
    def translating_matrix(self,x,y,z):
        matrix = copy.deepcopy(self.matrix)
        matrix[0][3] = self.matrix[0][3]+x
        matrix[1][3] = self.matrix[1][3]+y
        matrix[2][3] = self.matrix[2][3]+z
        return mat3d(matrix)

    def rotation_yz_matrix(self,angle):
        matrix = copy.deepcopy(self.matrix)
        matrix[1][2] = math.cos(angle)
        matrix[1][3] = math.sin(angle)
        matrix[2][2] = -math.sin(angle)
        matrix[2][3] = math.cos(angle)
        return mat3d(matrix)

    def rotation_zx_matrix(self,angle):
        matrix = copy.deepcopy(self.matrix)
        matrix[0][0] = math.cos(angle)
        matrix[0][3] = -math.sin(angle)
        matrix[2][0] = math.sin(angle)
        matrix[2][3] = math.cos(angle)
        return mat3d(matrix)

    def rotation_xy_matrix(self,angle):
        matrix = copy.deepcopy(self.matrix)
        matrix[0][0] = math.cos(angle)
        matrix[0][1] = math.sin(angle)
        matrix[1][0] = -math.sin(angle)
        matrix[1][1] = math.cos(angle)
        return mat3d(matrix)


"""
mat = mat3d([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
print(mat.scaling_matrix(2,2,3).matrix)
print(mat.translating_matrix(2).matrix)
print(mat.rotation_yz_matrix(45).matrix)
print(mat.matrix)
"""