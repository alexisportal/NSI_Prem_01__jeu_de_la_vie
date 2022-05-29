# -*- coding: utf-8 -*-
"""
Created on Sat May  7 00:21:01 2022

@author: tport
"""

def get_voisins (cases, i, j):
    voisins = \
                [cases[i-1][j+1], \
                 cases[i][j+1], \
                 cases[i+1][j+1], \
                 cases[i-1][j], \
                 cases[i+1][j], \
                 cases[i-1][j-1], \
                 cases[i][j-1], \
                 cases[i+1][j-1]]
    return voisins

def count_alive_voisins (voisins):
    cpt = 0
    for voisin in voisins:
        if is_alive (voisin):
            cpt = cpt + 1
    return cpt

def is_alive (case):
    return case==1
