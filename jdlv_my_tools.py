# automates cellulaires
# https://www.youtube.com/watch?v=yM_rfSg5DeY
# Bn / Sn
# B : naissance si n
# S : survie si n


from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *
from jdlv_main import *

#import winsound
#import random

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid



############################################################
#
#              MAKE_CONWAY
#
############################################################




################################################################
# Rule 30
################################################################

def make_conway_30 (grid, i, j, color):
    try:
        cases = grid.cases
        
        milieu = int(len(cases)/2)
        
        
        for i in range(len(cases)):
            for j in range(len(cases)):
                cases [i] [j] ['s'] = death_status
                cases [i] [j] ['c'] = death_color
        
        
        cases [len(cases)-1] [milieu] ['s'] = life_status
        cases [len(cases)-1] [milieu] ['c'] = life_color
 

    except:
        pass
    return grid







#################################################################
#
#                   JDLV
#
#################################################################



################################################################
# Rule 30
# https://www.youtube.com/watch?v=IK7nBOLYzdE
################################################################

def apply_game_of_life_rules_30 (grid,compteur):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases

    milieu = int(len(cases)/2)
    limite = int(len(cases)/10)*9


    ###############################################################
    # Décaler les lignes du bas vers le haut jusqu'à la moitié
    # de l'écran
    ###############################################################

    for i in range (limite+1, len (cases)):
        for j in range (1, len (cases) - 1):
            next_cases [i-1] [j]["s"] =  cases [i] [j]["s"]
            next_cases [i-1] [j]["c"] =  cases [i] [j]["c"]


    
    ###############################################################
    # Nouvelles règles pour la ligne du bas
    # 111 => 0
    # 110 => 0 
    # 101 => 0
    # 100 => 1
    # 011 => 1
    # 010 => 1
    # 001 => 1
    # 000 => 0
    ###############################################################

    for i in [len (cases) - 1]:
        for j in range (1, len (cases) - 1):
            voisins = get_voisins_30 (cases, i, j)
            
            g = voisins[0]
            m = voisins[1]
            d = voisins[2]
            
            if  (is_alive(g) and is_alive(m) and is_alive(d)) or \
                (is_alive(g) and is_alive(m) and is_dead(d)) or \
                (is_alive(g) and is_dead(m) and is_alive(d)) or \
                (is_dead(g) and is_dead(m) and is_dead(d)):
                    next_cases [i] [j]["s"] =  death_status
                    #next_cases [i] [j]["c"] =  death_color
                    
                    if j>milieu-compteur-1 and j<milieu+compteur+1:
                        next_cases [i] [j]["c"] =  death_color_bas
                    else:
                        next_cases [i] [j]["c"] =  death_color
                    
                    
            else:
                    next_cases [i] [j]["s"] =  life_status
                    next_cases [i] [j]["c"] =  life_color_bas





    ###############################################################
    # Règles de Conway pour les lignes 0 à la moitié de l'écran
    ###############################################################

    for i in range (1, limite):
        for j in range (1, len (cases) - 1):
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            
            c = cases [i] [j]
            
            if nbre_alive_voisins==3:
                    next_cases [i] [j]["s"] =  life_status
                    next_cases [i] [j]["c"] =  life_color

            else:
                if nbre_alive_voisins==2:
                    if is_alive(cases [i] [j]):
                        next_cases [i] [j]["s"] =  life_status
                        next_cases [i] [j]["c"] =  life_color
                    else:
                        next_cases [i] [j]["s"] =  get_next_death_status(cases[i][j],False)
                        next_cases [i] [j]["c"] =  get_next_death_color(next_cases[i][j])
                            
                    
                else:
                    if is_alive(cases[i][j]):
                        next_cases [i] [j]["s"] =  get_next_death_status(cases[i][j],True)
                        next_cases [i] [j]["c"] =  get_next_death_color(next_cases[i][j])
                    else:
                        next_cases [i] [j]["s"] =  get_next_death_status(cases[i][j],False)
                        next_cases [i] [j]["c"] =  get_next_death_color(next_cases[i][j])
    

    return next_grid




    
    

#################################################################
#
#                   APPLY_RULES
#
#################################################################


def apply_rules (grid, compteur):
    
    if compteur==0:
        next_grid = make_conway_30 (grid, 4, 4, life_color)
    else:
        # time.sleep (0.1)
        next_grid= apply_game_of_life_rules_30 (grid,compteur)

        
    return next_grid



