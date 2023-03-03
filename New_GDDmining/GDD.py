import numpy as np
import pandas as pd
import time
import itertools
import Levenshtein as ls
import re
import copy
from itertools import combinations
import operator
import glob


class Blocks(object):
    def __init__(self, Namelist, name, distance,tuples):
        self.Namelist = Namelist
        self.name = name
        self.distance = distance
        self.tuples = tuples

    def __repr__(self):
        return "%s %s %s %s" % (self.Namelist, self.name, self.distance, self.tuples)

class node_s(object):
    def __init__(self, id, name, attribute):
        self.id = id
        self.name = name
        self.attribute = attribute

    def __repr__(self):
        return "%s %s %s" % (self.id, self.name, self.attribute)


class snode(object):
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute

    def __repr__(self):
        return "%s %s" % (self.name, self.attribute)


class Dtems(object):
    def __init__(self, itemname, newname, items):
        self.name = itemname
        self.newname = newname
        self.sigma = items

    def __repr__(self):
        return "%s %s %s" % (self.name, self.sigma, self.newname)


class DD(object):

    def __init__(self, rhs: str, lhs: str, items):
        self.rhs = rhs
        self.lhs = lhs
        self.items = items

    def __repr__(self):
        return "%s %s %s" % (self.lhs, self.rhs, self.items)


class LCP(object):
    def __init__(self, level_name: str, items: list, cand: list):
        self.name = level_name
        self.items = items
        self.cand = cand

    def __repr__(self):
        return "%s %s %s " % (self.name, self.items, self.cand)


class iteml(object):
    def __init__(self, itemname: str, sigma, l, shares):
        self.name = itemname
        self.sigma = sigma
        self.l = l
        self.shares = shares

    def __repr__(self):
        return "%s %s %s %s" % (self.name, self.sigma, self.l, self.shares)

class Block:
    '''
    the strcture of one block of each lattice level
    '''

    def __init__(self, attributeLabels, literalsSet):
        self.attributeLabels = attributeLabels
        self.literalsSet = literalsSet

    def __repr__(self):
        return str(self.attributeLabels)
