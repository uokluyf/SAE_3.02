import networkx as nx
import matplotlib.pyplot as plt

fichier_entrant = open("Entrée.txt", "r")
lignes = fichier_entrant.readlines()
bornes = {}

for ligne in lignes:
    ligne = ligne.split()
    bornes[ligne[0]]={"pos_x": int(ligne[1]), "pos_y": int(ligne[2]), "rayon" : int(ligne[3]), "color" : "white"}
    with open("Sortie.txt", "w") as fichier_sortant:
        for n,borne in bornes.items():
            fichier_sortant.write(f"{n} {borne['color']}\n")



