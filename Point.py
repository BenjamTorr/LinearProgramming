import matplotlib
import numpy
import math as m

EPS = 0.00001

class Point:
    def __init__(self, a_x, a_y):
        self.x = a_x
        self.y = a_y
        
    def __eq__(self, a):
        if(self.x == a.x and self.y == a.y):
            return True
        else:
            return False
        
    def collinear(p, q, r):
        return (abs(Vec.cross(Vec(p,q),Vec(p,r)))) < EPS
        
class Vec:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y
        
    #producto cruz de dos vectores
    def cross( a, b):
        return a.x * b.y - a.y * b.x
    
    # regresa si el punto se encuentra a la izqueirda
    def ccw(p, q, r):
        return (Vec.cross(Vec(p,q),Vec(p,r))) >= 0
    
    #regresa el producto punto
    def dot(a, b):
        return a.x * b.x + a.y * b.y
    
    def norm_sq(self):
        return self.x * self.x + self.y * self.y
    
    def angle(a, o, b):
        oa = Vec(o, a)
        ob = Vec(o, b)
        return m.acos(Vec.dot(oa, ob) / m.sqrt(oa.norm_sq() * ob.norm_sq()))
    
