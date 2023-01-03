import math
import networkx as nx
import matplotlib.pyplot as plt

"""
3em étape : programmer l'algorithme de Welsh Powell
 => condition = distance > rayon max des 2 bornes
"""


bornes_exemple = {
        "1":{"pos_x": 1, "pos_y": 2, "rayon" : 1, "color" : "white"},
        "2":{"pos_x": 3, "pos_y": 1, "rayon" : 2, "color" : "white"},
        "3":{"pos_x": 0, "pos_y": 0, "rayon" : 4, "color" : "white"},
        "4":{"pos_x": 7, "pos_y": 4, "rayon" : 1, "color" : "white"}
          }
""""
Theoriquement en sortie :

borne   color
1       2
2       2
3       1
4       1
"""

""""
==========================================
----------------Traitement---------------
==========================================
"""


def Creation_Graph(bornes):
    G = nx.Graph()

    #Creation des Sommets======================================================================================
    for s, attr in bornes.items():
        G.add_node(s, pos_x=attr['pos_x'], pos_y=attr['pos_y'], rayon=attr['rayon'], color=attr['color'])

    #Creation des arrêtes entre bornes superposés==============================================================
    for s1, attr1 in bornes.items():
            for s2, other_attr in bornes.items():
                if s2 != s1: #pour empêcher les boubles
                    distance = math.sqrt((abs(attr1["pos_x"] - other_attr["pos_x"]))**2 + (abs(attr1["pos_y"] - other_attr["pos_y"]))**2)
                    #print(f"{s1} => {s2} : {distance}")
                    if distance < attr1["rayon"] or distance < other_attr["rayon"] :
                        G.add_edge(s1, s2)


    pos = nx.planar_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)

    plt.show()

    return G

def Welsh_Powell(G, bornes):
    #étape 1 : trier par ordre croissant
    degree_nodes_list = G.degree()

    sorted_nodes_tuple = sorted(degree_nodes_list, key=lambda degree: degree[1], reverse=True) #https://docs.python.org/fr/3.6/howto/sorting.html
    sorted_nodes = []
    for u,v in sorted_nodes_tuple:
        sorted_nodes.append(u)
    #print(sorted_nodes)

    # étape 2 : attribuer les couleurs
    color = 1
    for n in sorted_nodes:
        print( bornes[n])
        if bornes[n]["color"] =="white":
            bornes[n]["color"] = color
            print(bornes[n])
            for m in bornes.keys():
                if m not in G[n].keys() and bornes[m]["color"] == "white":
                    bornes[m]["color"] = bornes[n]["color"]
                    print(f"Impossible de {n} => {m} = {bornes}")
        color += 1







G = Creation_Graph(bornes_exemple)

Welsh_Powell(G, bornes_exemple)

print(bornes_exemple)









""""
==========================================
--------------------NOTE------------------
==========================================


def Welsh_Powell_V1(bornes):
    color = 1
    for n,borne in bornes.items():
        if borne["color"]=="white":
            borne["color"] = color
            for m,other_borne in bornes.items():
                distance = math.sqrt((abs(borne["pos_x"] - other_borne["pos_x"]))**2 + (abs(borne["pos_y"] - other_borne["pos_y"])**2)) #calcul distance entre 2 bornes
                print(f"distance entre {n} et {m} = {distance} ")
                if distance > borne["rayon"] or distance > other_borne["rayon"] and other_borne[color] == "white":
                    other_borne["color"] = borne["color"]
                    #print(f"en partant de {n} => {bornes}")
        color += 1

    return bornes
"""

#print(f"AU final : {Welsh_Powell_V1(bornes_exemple)}")






"""
add_edge(k,p)

add_node()
"""