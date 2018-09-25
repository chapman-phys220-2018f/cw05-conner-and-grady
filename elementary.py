#!/usr/bin/env python

class particle(object):
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)
    def __init__(self, x, y, z):
        self.position = (x,y,z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        self.momentum = self.momentum + (px,py,pz)

    def move(self, dt):
        self.position = self.position + dt*self.momentum

def main(argv):

