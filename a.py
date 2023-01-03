import matplotlib.pyplot as plt
import networkx as nx

# Créer un graphe à l'aide de NetworkX
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4), (1, 5), (1, 6), (2, 4), (3, 4), (5, 4), (6, 4), (2, 5), (3, 5), (6, 5), (2, 6), (3, 6)])

# Dessiner le graphe à l'aide de Matplotlib
pos = nx.spring_layout(G, k=10)
nx.draw(G, pos, with_labels=True)

# Charger l'image que vous voulez utiliser en tant que fond d'écran
image = plt.imread('mon_image.webp')

# Créer une figure Matplotlib et définir l'image comme fond d'écran
fig, ax = plt.subplots()
ax.imshow(image, extent=[0, 15, 0, 15])

# Ajouter le graphe au-dessus de l'image en utilisant les mêmes coordonnées de position que précédemment
nx.draw(G, pos, ax=ax, node_size=200)

# Afficher le graphe
plt.show()