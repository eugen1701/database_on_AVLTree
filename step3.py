# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:36:03 2020

@author: Quentin
"""

import numpy as np

# Vertices :
v_step3 = ['Upper E',
       'Reactor',
       'Lower E',
       'Security',
       'Medbay',
       'Electrical',
       'Storage',
       'Cafeteria',
       'Admin',
       'Comms',
       'Shield',
       'O2',
       'Weapons',
       'Navigations']

# Edges for the crewmates :
e_step3 = [('Upper E','Reactor',19),
      ('Upper E','Security',18),
      ('Upper E','Lower E',31),
      ('Reactor','Security',21),
      ('Reactor','Lower E',20),
      ('Lower E','Security',19),
      ('Upper E','Medbay',24),
      ('Upper E','Cafeteria',42),
      ('Medbay','Cafeteria',25),
      ('Lower E','Electrical',23),
      ('Lower E','Storage',39),
      ('Electrical','Storage',18),
      ('Cafeteria','Storage',36),
      ('Cafeteria','Admin',27),
      ('Storage','Admin',20),
      ('Storage','Shield',29),
      ('Storage','Comms',17),
      ('Comms','Shield',16),
      ('Cafeteria','Weapons',25),
      ('Weapons','O2',14),
      ('Weapons','Shield',34),
      ('Weapons','Navigations',24),
      ('O2','Navigations',27),
      ('O2','Shield',23),
      ('Navigations','Shield',28)]

# Edges for the impostors :
e_step3_imp = [('Upper E','Reactor',0),# changed to 0
      ('Upper E','Security',18),
      ('Upper E','Lower E',31),
      ('Reactor','Security',21),
      ('Reactor','Lower E',0),# changed to 0
      ('Lower E','Security',19),
      ('Upper E','Medbay',24),
      ('Upper E','Cafeteria',42),
      ('Medbay','Cafeteria',25),
      ('Lower E','Electrical',23),
      ('Lower E','Storage',39),
      ('Electrical','Storage',18),
      ('Cafeteria','Storage',36),
      ('Cafeteria','Admin',0),# changed to 0
      ('Storage','Admin',20),
      ('Storage','Shield',29),
      ('Storage','Comms',17),
      ('Comms','Shield',16),
      ('Cafeteria','Weapons',18),# changed to 18
      ('Weapons','O2',14),
      ('Weapons','Shield',34),
      ('Weapons','Navigations',0),# changed to 0
      ('O2','Navigations',27),
      ('O2','Shield',23),
      ('Navigations','Shield',0),# changed to 0
      ('Security','Medbay',0),# added
      ('Electrical','Medbay',0),# added
      ('Security','Electrical',0),# added
      ('Cafeteria','Navigations',20),# added
      ('Cafeteria','O2',9),# added
      ('Cafeteria','Shield',16),# added
      ('Admin','O2',9),# added
      ('Admin','Navigations',20),# added
      ('Admin','Shield',16),# added
      ('Admin','Weapons',18)# added
      ]

# Method to add the reverse edges :
def undirected_graph(e_step3):
    e2 = e_step3.copy()
    for edge in e_step3:
        u,v,w = edge
        e2.append((v,u,w))
    return e2

def floyd_warshall(graph):
    v_step3=graph[0]
    e_step3=graph[1]
    # We convert the directed graph into a directed graph
    e_step3=undirected_graph(e_step3)
    # Initializing the matrix : inf for the distances and NIL for the parents
    graph = [[float('inf') for x in range(len(v_step3))] for y in range(len(v_step3))]
    parent = [['NIL' for x in range(len(v_step3))] for y in range(len(v_step3))]
    # For each vertex, the distance to itself is 0
    for i in range(len(v_step3)):
        for j in range(len(v_step3)):
            if i == j:
                graph[i][j]=0
    # For each edge, put the weight in the corresponding cell
    # And put the source vertex in the corresponding cell of the parents matrix
    for (src,dst,w) in e_step3:
        graph[v_step3.index(src)][v_step3.index(dst)] = w
        parent[v_step3.index(src)][v_step3.index(dst)] = str(src)
    # Starting the Floyd-Warshall algo !
    for k in range(len(v_step3)):
        # For each source vertex,
        for i in range(len(v_step3)):
            # And for each destination vertex of the source vertex :
            for j in range(len(v_step3)):
                # If k is on the shortest path from the source vertex to the destination vertex,
                # Update the value of the distance matrix and the parents matrix !
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    parent[i][j] = parent[k][j]
    print(np.array(graph))
    for line in parent:
        print(line)

# print("\n\n\n************************Crewmates************************\n\n")
# graph=v_step3,e_step3
# floyd_warshall(graph)
# print("\n\n\n************************Impostors************************\n\n")
# graph=v_step3,e_step3_imp
# floyd_warshall(graph)