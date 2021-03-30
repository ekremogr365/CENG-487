# -*- coding: utf-8 -*-
# CENG 487 Assignment3 by
# Ekrem Ozturk
# StudentId: 240201006
# 12 2020

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
           
            
"""
abc = mat3d([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
triangle = objct(vec3d(-1.5, 0.0, -6.0, 1.0), # Position
[ # Vertices
	vec3d(0.0, 1.0, 0.0, 1.0), 			# Top
	vec3d(1.0, -1.0, 0.0, 1.0),			# Bottom Right
	vec3d(-1.0, -1.0, 0.0, 1.0),		# Bottom Left
], [ # matrix stack
mat3d.translating_matrix(abc,0,-2,0)
])
print(mat3d.translating_matrix(abc,0,-1,0).matrix)

triangle.applyMatrixStack()

print(triangle.vertices[0].x,triangle.vertices[0].y,triangle.vertices[0].z)
print(triangle.vertices[1].x,triangle.vertices[1].y,triangle.vertices[1].z)
print(triangle.vertices[2].x,triangle.vertices[2].y,triangle.vertices[2].z)


xx = mat3d([[1, 0, 0, 0], [0, 1, 0, -1], [0, 0, 1, 0], [0, 0, 0, 1]])
print(xx.multiply(vec3d(0.0, 1.0, 0.0, 1.0)).y)
"""
