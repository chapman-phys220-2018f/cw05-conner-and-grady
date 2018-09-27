#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####
# Conner Carnahan and Grady
# Email: carna104@mail.chapman.edu
# Elementary module for CW 5
# PHYS 220
# Septemeber 27, 2018
####

import scipy.constants

class particle(object):
    """Particle is a class that should have 3 initialized variables: Mass(a float), Position(A triplet of floats), Momentum(A triplet of floats)"""
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)
    def __init__(self, x, y, z):
        """Inits the class, arg1: x position float, arg2: y position float, arg3: z positionfloat"""
        self.position = (x,y,z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        """changes the momentum by an increment arg1: px, arg2: py, arg3: pz"""
        self.momentum = self.momentum + (px,py,pz)

    def move(self, dt):
        """Moves the particle by a specified amount of time, it is calculated by taking the momentum of the particle and calculating the velocity
        times arg1: dt"""
        self.position = (self.position[0] + (dt/self.mass)*self.momentum[0],self.position[1]+(dt/self.mass)*self.momentum[1],self.position[2]+(dt/self.mass)*self.momentum[2])

class chargedparticle(particle):
    charge = 0.0

    def __init__(self, x,y,z):
        """uses the super constructor to construct the class instance
        arg1: x pos (float)
        arg2: y pos (float)
        arg3: z pos (float)
        sets the charge by default to 0"""
        particle.__init__(x,y,z)
        self.charge = 0.0

def main(argv):
    pass


