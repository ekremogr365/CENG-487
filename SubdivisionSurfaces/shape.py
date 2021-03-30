# -*- coding: utf-8 -*-
# CENG 487 Assignment4 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

import random
from vec3d import vec3d


class objct :
    def __init__(self, position,vertices,matrix_stack):
        self.position = position
        self.vertices = vertices
        self.matrix_stack=matrix_stack
        self.color = vec3d(random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1),1)
        
    def applyMatrixToVertices(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.multiply(vertex)
            
    def applyMatrixStack(self):
        for matrix in self.matrix_stack:
            self.applyMatrixToVertices(matrix)
           
