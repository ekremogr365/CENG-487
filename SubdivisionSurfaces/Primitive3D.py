# -*- coding: utf-8 -*-
# CENG 487 Assignment4 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

from shape import objct
from vec3d import vec3d
from mat3d import mat3d
from subDivideCC import *

class Primitive3D:
    
    def __init__(self, *inp):
        
        if(len(inp)==1):
            self.shapes = inp[0]
        if(len(inp)==3):
            self.shapes = inp[0]      
            self.faces = inp[1]
            self.vertices = inp[2]
    
    def subdivideShapes(self,numDivision):
        newShapes = []
        for shape in self.shapes:
            newShape = objct(shape.position,[],shape.matrix_stack)
            vertices = shape.vertices
            betweenlen_x = ((vertices[1].x-vertices[0].x))/numDivision
            betweenlen_y = ((vertices[1].y-vertices[0].y))/numDivision     
            betweenlen_z = ((vertices[1].z-vertices[0].z))/numDivision


            all_vertices =[]
            if(betweenlen_x==0.0):
                betweenlen_x = ((vertices[3].x-vertices[0].x))/numDivision
            if(betweenlen_y==0.0):
                betweenlen_y = ((vertices[3].y-vertices[0].y))/numDivision
            if(betweenlen_z==0.0):
                betweenlen_z = ((vertices[3].z-vertices[0].z))/numDivision


            all_vertices =self.divideXY(numDivision,betweenlen_x,betweenlen_y,vertices[0])
            all_vertices =self.divideXZ(numDivision,betweenlen_x,betweenlen_z,vertices[0])
            all_vertices=self.divideYZ(numDivision,betweenlen_y,betweenlen_z,vertices[0])
        
            
            
            newShapes += self.verticesToQuads(all_vertices, shape)
        self.shapes = newShapes
        #return newShapes
    
    
    def divideXY(self,divideNum,len_x,len_y,initial_point): 
        vertices = [[0 for x in range(divideNum+1)] for y in range(divideNum+1)] 
        initial_x = initial_point.x
        initial_y = initial_point.y
        for i in range(divideNum+1):
            y = initial_y + (len_y*i)
            for j in range(divideNum+1):
                x = initial_x + (len_x*j)
                vec = vec3d(x, y, initial_point.z, 1.0)
                vertices[i][j] = vec

        return vertices;
    
    def divideXZ(self,divideNum,len_x,len_z,initial_point):
        
        vertices = [[0 for x in range(divideNum+1)] for y in range(divideNum+1)] 
        initial_x = initial_point.x
        initial_z = initial_point.z
        for i in range(divideNum+1):
            
            z = initial_z + (len_z*i)
            for j in range(divideNum+1):
                x = initial_x + (len_x*j)
                vec = vec3d(x, initial_point.y, z, 1.0)
                vertices[i][j] = vec

        return vertices;
    
    def divideYZ(self,divideNum,len_y,len_z,initial_point):
        
        vertices = [[0 for x in range(divideNum+1)] for y in range(divideNum+1)] 
        initial_y = initial_point.y
        initial_z = initial_point.z
        for i in range(divideNum+1):
            
            z = initial_z + (len_z*i)
            for j in range(divideNum+1):
                y = initial_y + (len_y*j)
                vec = vec3d(initial_point.x, y, z, 1.0)
                vertices[i][j] = vec

        return vertices;
    
    def verticesToQuads(self,all_vertices,inital_shape):
        
        shapes = []
        for i in range(len(all_vertices)-1):
            for j in range(len(all_vertices)-1):
                vertices = [all_vertices[i][j],all_vertices[i+1][j], all_vertices[i+1][j+1],all_vertices[i][j+1]]
                shape = objct(inital_shape.position, vertices,inital_shape.matrix_stack)
                shapes.append(shape)
                
        return shapes
  
    
    def sub_division_v2(self,numDivision):
        newShapes = []
        for shape in self.shapes:
            newShape = objct(shape.position,[],shape.matrix_stack)
            vertices = shape.vertices
            betweenlen_x = ((vertices[1].x-vertices[0].x))/numDivision
            betweenlen_y = ((vertices[1].y-vertices[0].y))/numDivision     
            betweenlen_z = ((vertices[1].z-vertices[0].z))/numDivision   
            vertices_edge_1 = self.find_middle_vertices(vec3d(round(betweenlen_x,3),round(betweenlen_y,3),round(betweenlen_z,3),1),vertices[0],vertices[1],numDivision)
        
            betweenlen_x = ((vertices[2].x-vertices[1].x))/numDivision
            betweenlen_y = ((vertices[2].y-vertices[1].y))/numDivision     
            betweenlen_z = ((vertices[2].z-vertices[1].z))/numDivision   
            vertices_edge_2 = self.find_middle_vertices(vec3d(round(betweenlen_x,3),round(betweenlen_y,3),round(betweenlen_z,3),1),vertices[1],vertices[2],numDivision)

            betweenlen_x = ((vertices[3].x-vertices[2].x))/numDivision
            betweenlen_y = ((vertices[3].y-vertices[2].y))/numDivision     
            betweenlen_z = ((vertices[3].z-vertices[2].z))/numDivision   
            vertices_edge_3 = self.find_middle_vertices(vec3d(round(betweenlen_x,3),round(betweenlen_y,3),round(betweenlen_z,3),1),vertices[2],vertices[3],numDivision)

            betweenlen_x = ((vertices[0].x-vertices[3].x))/numDivision
            betweenlen_y = ((vertices[0].y-vertices[3].y))/numDivision     
            betweenlen_z = ((vertices[0].z-vertices[3].z))/numDivision   
            vertices_edge_4 = self.find_middle_vertices(vec3d(round(betweenlen_x,3),round(betweenlen_y,3),round(betweenlen_z,3),1),vertices[3],vertices[0],numDivision)

            vertices_between = []
            for i in range(len(vertices_edge_2)):
                 betweenlen_x = ((vertices_edge_2[i].x-vertices_edge_4[len(vertices_edge_2)-1-i].x))/numDivision
                 betweenlen_y = ((vertices_edge_2[i].y-vertices_edge_4[len(vertices_edge_2)-1-i].y))/numDivision     
                 betweenlen_z = ((vertices_edge_2[i].z-vertices_edge_4[len(vertices_edge_2)-1-i].z))/numDivision 
                     
                 vertices_edge_middle = self.find_middle_vertices(vec3d(round(betweenlen_x,3),round(betweenlen_y,3),round(betweenlen_z,3),1),vertices_edge_4[i],vertices_edge_2[len(vertices_edge_2)-1-i],numDivision)
                 vertices_between.append(vertices_edge_middle)
    
            newShapes +=  self.edges_to_shapes(vertices_between,shape)
        self.shapes = newShapes


    def edges_to_shapes(self,edge_vertices,inital_shape):
        shapes = []
        for i in range(len(edge_vertices)-1):
            for j in range(len(edge_vertices)-1):
                vertices = [edge_vertices[i][j],edge_vertices[i][j+1], edge_vertices[i+1][j+1],edge_vertices[i+1][j]]
                shape = objct(inital_shape.position, vertices,inital_shape.matrix_stack)
                shapes.append(shape)
        return shapes

    def find_middle_vertices(self,vec_len,vec_vert1,vec_vert2,numD):
        vertices = []
        vertices.append(vec_vert1)
        for i in range(numD-1):
            newX=vec_vert1.x+vec_len.x
            newY=vec_vert1.y+vec_len.y
            newZ=vec_vert1.z+vec_len.z
            vec_vert1= vec3d(round(newX,3),round(newY,3),round(newZ,3),1)
            vertices.append(vec_vert1)
        vertices.append(vec_vert2)
        return vertices


    def face_and_vertices_to_shapes(self,tori_face_vertex_indes, vertices):
        shapes = []
        faces = []
        
        for face_indexes in tori_face_vertex_indes:
            face = [face_indexes[0]+1,face_indexes[1]+1,face_indexes[2]+1,face_indexes[3]+1]
            faces.append(face)
            
        for face_indexes in faces:
            shape = objct(vec3d(0.0,0.0,0.0, 1.0),[],[])
            for face_index in face_indexes:
                x = vertices[face_index-1][0]
                y = vertices[face_index-1][1]
                z = vertices[face_index-1][2]
                vec = vec3d(x,y,z,1)
                shape.vertices.append(vec)
            shapes.append(shape)
        return shapes

    def subdivide_cmc(self,numdivision):
        
        face_list = []
        
        for face in self.faces:
            index_list = [face[0]-1,face[1]-1,face[2]-1,face[3]-1]    
            face_list.append(index_list)
        
        output_points, output_faces = self.vertices,face_list
        for i in range(numdivision-1):
            output_points, output_faces = cmc_subdiv(output_points, output_faces)
        
        self.shapes = self.face_and_vertices_to_shapes(output_faces,output_points)



initial = mat3d([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
 
square1 = objct(vec3d(1.1, 1.0, -8.0, 1.0), # Position
[ # Vertices
	vec3d(-1.4, 1.0, -0.4, 1.0),	
	vec3d(1.0, 1.0, -1.0, 1.0),			
	vec3d(1.0, -1.0, -1.0, 1.0),
	vec3d(-1.4, -1.0, -0.4, 1.0),			

], [ # matrix stack
    mat3d.translating_matrix(initial,-1, 1.0, 0.0),
    mat3d.rotation_zx_matrix(initial,0.01),
   	mat3d.translating_matrix(initial,1.0, -1.0, 0.0)

])
