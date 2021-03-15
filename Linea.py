import math as m
import matplotlib
import numpy as np
import Point as Po

class Linea:
    def __init__(self, p, c, is_y0):
        self.m = p
        self.b = c
        self.y0 = is_y0

    def eval(self, x):
        return  self.m * x + self.b

    def __eq__(self, b):
        return self.m == b.m and self.b == a.b

    def obtenLinea(a, b):
        if a.x == b.x:
            return Linea(1, -a.x, True)
        else:
            k = (b.y - a. y) / (b.x - a.x)
            return Linea(k, a.y - k * a.x, False)

    def interseca(self, q):
        if(self.y0 == True):
            if(q.y0 == True):
                return "Colineales"
            return Po.Point(-self.b, q.eval(-self.b))
        if(q.y0 == True):
            return Po.Point(-q.b, self.eval(-q.b))
        if(self.m == q.m):
            return "Colineales"
        else:
            k = (q.b - self.b) /(self.m - q.m)
            return Po.Point(k, self.eval(k))

