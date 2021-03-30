# -*- coding: utf-8 -*-
# CENG 487 Assignment5 by
# Ekrem Ozturk
# StudentId: 240201006
# 01 2021



class Light:
    
    def __init__(self, position,procudurelLen):
        
        self.procudurelLen = procudurelLen
        self.position = position
        self.new_pos = position
        self.direction = "up"

        
        
    def calculate_new_pos_X(self):
        x = self.position
        if (self.new_pos[0]+0.1) > (x[0] +self.procudurelLen):
            self.direction ="down"
        if (self.new_pos[0]-0.1) < (x[0] - self.procudurelLen):
            self.direction = "up"
            

        if self.direction == "up":
            new_x = self.new_pos[0]+0.1
        if self.direction == "down":
            new_x = self.new_pos[0]-0.1
        self.new_pos = [new_x,x[1],x[2]]
        return self.new_pos
    
    def calculate_new_pos_Y(self):
        x = self.position
        if (self.new_pos[1]+0.1) > (x[1] +self.procudurelLen):
            self.direction ="down"
        if (self.new_pos[1]-0.1) < (x[1] - self.procudurelLen):
            self.direction = "up"
            

        if self.direction == "up":
            new_y = self.new_pos[1]+0.1
        if self.direction == "down":
            new_y = self.new_pos[1]-0.1
        self.new_pos = [x[0],new_y,x[2]]
        return self.new_pos
    