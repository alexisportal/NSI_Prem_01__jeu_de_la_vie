########################################
# Création de la structure de donnée                                     
########################################

from jdlv_data import *

class Grid ():
    def __init__ (self, N):
        self.cases = self.make_data (N)

    def make_data (self, N):
        cases = []
        for i in range (N):
            cases.append ([])
            for j in range (N):
                case = {}
                case ['s'] = death_status
                case ['c'] = death_color
                cases [i].append (case)
        return cases

    def fill_grid_with_cases (self, other_cases):
        for i in range (len (other_cases)):
            if i > len (self.cases) - 1:
                self.cases.append ([])
            for j in range (len (other_cases)):
                try:
                    self.cases [i] [j] = other_cases [i] [j]
                except:
                    case = {}
                    case ['s'] = other_cases [i] [j] ['s']
                    case ['c'] = other_cases [i] [j] ['c']
                    self.cases [i].append (case)
