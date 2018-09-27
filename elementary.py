#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####
# Conner Carnahan and Grady
# Email: carna104@mail.chapman.edu
# 
#

class particle(object):
    """Particle is a class that should have 3 initialized variables: Mass(a float), Position(A triplet of floats), Momentum(A triplet of floats)"""
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)
    def __init__(self, x, y, z):
        """Inits the class, arg1 is self (does something that has to do with self reference), arg2: x position float, arg3: y position float, arg4: z positionfloat"""
        self.position = (x,y,z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        """changes the momentum by """
        self.momentum = self.momentum + (px,py,pz)

    def move(self, dt):
        self.position = self.position + dt*self.momentum

def main(argv):

