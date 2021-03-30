# -*- coding: utf-8 -*-
# CENG 487 Assignment5 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021

from shape import objct
from vec3d import vec3d
from Primitive3D import Primitive3D


class ObjParser:
    
    def __init__(self, file_name):
        self.file_name = file_name

    
    def parse_file(self):
    
        tori_file = open(self.file_name, "r")
        tori_file_lines = tori_file.readlines()
        tori_face_vertex_indes = []
        tori_vertecies = []
        shapes = []
        for line in tori_file_lines:
            if(line[0]=='f'):
                whiteSpaceRegex = " ";
                line_array = line.split(whiteSpaceRegex);
                line_array.pop(0)
                line_array[3] = line_array[3].rstrip("\n")
                line_array[0] = int(line_array[0])
                line_array[1] = int(line_array[1])
                line_array[2] = int(line_array[2])
                line_array[3] = int(line_array[3])
        
                tori_face_vertex_indes.append(line_array)
             
                
        for line in tori_file_lines:
            if(line[0]=='v'):
                whiteSpaceRegex = " ";
                line_array = line.split(whiteSpaceRegex);
                line_array.pop(0)
                line_array[2] = line_array[2].rstrip("\n")
                line_array[0] = float(line_array[0])
                line_array[1] = float(line_array[1])
                line_array[2] = float(line_array[2])
                tori_vertecies.append(line_array)
        tori_file.close()
        
        for face_indexes in tori_face_vertex_indes:
            shape = objct(vec3d(0.0,0.0,0.0, 1.0),[],[])
            for face_index in face_indexes:
                x = tori_vertecies[face_index-1][0]
                y = tori_vertecies[face_index-1][1]
                z = tori_vertecies[face_index-1][2]
                vec = vec3d(x,y,z,1)
                shape.vertices.append(vec)
            shapes.append(shape)
        return [shapes,tori_face_vertex_indes,tori_vertecies]
    
class ObjParserTriangleMultiplePrim:
    
    def __init__(self, file_name):
        self.file_name = file_name

    
    def parse_file(self):
    
        tori_file = open(self.file_name, "r")
        tori_file_lines = tori_file.readlines()
        tori_face_vertex_indes = []
        tori_vertecies = []
        shapes = []
        prims_shapes = []
        primitivesLines = []
        primitiveLines = []
        primindex = 1
        g_default_index = 0
        for line in tori_file_lines:
            whiteSpaceRegex = " ";
            line_array = line.split(whiteSpaceRegex)
            if line_array[0] == "g" and line_array[1] == "default\n":
                g_default_index+=1
            if primindex == g_default_index:
                primitiveLines.append(line)
            elif g_default_index > 0:
                primitivesLines.append(primitiveLines)
                primitiveLines = []
                primindex +=1
        primitivesLines.append(primitiveLines)

        for primitiveLines in primitivesLines:
            for line in primitiveLines:
                if(line[0]=='f'):
                    whiteSpaceRegex = " ";
                    line_array = line.split(whiteSpaceRegex);
                    line_array.pop(0)
                    line_array[2] = line_array[2].rstrip("\n")
                    line_array[0] = int(line_array[0])
                    line_array[1] = int(line_array[1])
                    line_array[2] = int(line_array[2])
            
                    tori_face_vertex_indes.append(line_array)
    
            for line in tori_file_lines:
                if(line[0]=='v'):
                    whiteSpaceRegex = " ";
                    line_array = line.split(whiteSpaceRegex);
                    line_array.pop(0)
                    line_array[2] = line_array[2].rstrip("\n")
                    line_array[0] = float(line_array[0])/2
                    line_array[1] = float(line_array[1])/2
                    line_array[2] = float(line_array[2])/2
                    tori_vertecies.append(line_array)
            tori_file.close()
            
            for face_indexes in tori_face_vertex_indes:
                shape = objct(vec3d(0.0,0.0,0.0, 1.0),[],[])
                for face_index in face_indexes:
                    x = tori_vertecies[face_index-1][0]
                    y = tori_vertecies[face_index-1][1]
                    z = tori_vertecies[face_index-1][2]
                    vec = vec3d(x,y,z,1)
                    shape.vertices.append(vec)
                shapes.append(shape)
                
            prims_shapes.append(shapes)
            tori_face_vertex_indes = []
            shapes = []
        return prims_shapes
    
