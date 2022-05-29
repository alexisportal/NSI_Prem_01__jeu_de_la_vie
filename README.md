# game_of_life

Participants
============
Alexis PORTAL

    
Description
===========
J'ai refait le programme qui est présenté dans la vidéo https://www.youtube.com/watch?v=IK7nBOLYzdE:
- Les lignes de 0 jusqu'à une limite de l'écran suivent l'algorithme de Conway
    * si la cellule a 3 voisins en vie, elle est en viellipsis
    * si la cellule a 2 voisins en vie
        * si la cellule est en vie, elle reste en viellipsis
        * si la cellule est morte, elle reste morte
    * sinon la cellule meure ou reste morte
    
- Les lignes cette limite+1 jusqu'à l'avant dernière ligne sont décalées vers le haut
- La dernière ligne suit les règles suivantes :
    # ligne du dessus   => cellule (X en vie, O morte)
    # XXX               => O
    # XXO               => O 
    # XOX               => O
    # XOO               => X
    # OXX               => X
    # OXO               => X
    # OOX               => X
    # OOO               => O


jdlv_my_tools.py
================

    apply_rules (grid, compteur)
    ============================
    Lorsque le compteur est = 0, la fonction make_conway_30 est appelée pour afficher un point
    au milieu de la ligne du bas de l'écran.
    Sinon à chaque tour, la fonction apply_game_of_life_rules_30 calcule la prochaine grille.
            

    apply_game_of_life_rules_30 (grid,compteur)
    ===========================================
    - Cette fonction calcule la prochaine grille:
        * des lignes 0 à une limite : Conway
        * des lignes limite+1 à l'avant dernière ligne décalage vers le haut
        * Pour la dernière ligne, regarder la description
        
    - Gestion de la couleur des cellules mortes
        * dans jdlv_data.py
            * life_status
                * 0 corresponde à une cellule en vie
                * 1 corresponde à une cellule morte noir
                * les valeurs > 1 correspondentà une cellule qui est en train de mourrir (couleur qui va vers le noDeprecationWarning)
                
        * Si la cellule a le statut death_status
            * Si elle passe de life_status à death_status alors on l'indique à la fonction get_next_death_status
            
    get_next_death_status(cases,isnewdead)
    ======================================
    * Si la cellule vient de passer de life_status à death_status, elle prend le statut 2
    * Si la cellule a le statut death_status, elle reste dans ce statut
    * Si la cellule a un statut > 1 alors son statut est statut+1 (passe à la couleur suivante de la liste jdlv_data.colors)
    * Si le statut de la cellule > max_death_color, alors il repasse à death_statut (elle restera noire)
    
    get_next_death_color(cases)
    ===========================
    Cette fonction renvoie la couleur dans la liste jdlv_data.colors qui correspond au statut de la cellule
                                                                   
    
Corrections
===========
* Le programme ne fonctionnait plus lorsque j'ai changé les valeurs de life_status et death_status car
  la fonction jdlv_controleur.action_tablew_grid_itemSelectionChanged n'utilisait pas death_status mais la valeur
  0
* dans jdlv_vue_fromUI.setupUI, j'ai ajouté la ligne suivante pour enlever le cadrillage blanc
    self.tablew_grid.setShowGrid(False)

     
    
