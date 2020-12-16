# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:40:37 2020

@author: Quentin
"""
import numpy as np

# Vertices :
v_step4 = ['Admin',
       'Upper E',
       'Reactor',
       'Lower E',
       'Security',
       'Medbay',
       'Electrical',
       'Storage',
       'Cafeteria',
       'Comms',
       'Shield',
       'O2',
       'Weapons',
       'Navigations']

# Edges for the crewmates :
e_step4 = [('Upper E','Reactor'),
      ('Upper E','Security'),
      ('Upper E','Lower E'),
      ('Reactor','Security'),
      ('Reactor','Lower E'),
      ('Lower E','Security'),
      ('Upper E','Medbay'),
      ('Upper E','Cafeteria'),
      ('Medbay','Cafeteria'),
      ('Lower E','Electrical'),
      ('Lower E','Storage'),
      ('Electrical','Storage'),
      ('Cafeteria','Storage'),
      ('Cafeteria','Admin'),
      ('Storage','Admin'),
      ('Storage','Shield'),
      ('Storage','Comms'),
      ('Comms','Shield'),
      ('Cafeteria','Weapons'),
      ('Weapons','O2'),
      ('Weapons','Shield'),
      ('Weapons','Navigations'),
      ('O2','Navigations'),
      ('O2','Shield'),
      ('Navigations','Shield')]

# Method to add the reverse edges :
def undirected_graph(e_step4):
    e2 = e_step4.copy()
    for edge in e_step4:
        u,v = edge
        e2.append((v,u))
    return e2

# Method to convert a graph represented by v and e to an adjacency matrix :
def adjacencyMat(v,e_step4):
    graph = np.zeros((len(v),len(v)),dtype=int)
    for (src,dst) in e_step4:
        graph[v.index(src)][v.index(dst)] = 1
    return graph

def hamiltonianPath(graph,v,path,i):
    # If all vertices are included in the path, the path is done.
    if i == len(v):
         return True
    for vertex in v[1:]: # We removed the first room, because it is already in the path
        # If the vertex is adjacent to the last vertex in the path and if
        # it is not already in the path, we add it.
        # If we are in a dead end (no adjacent vertex meet the conditions,
        # we backtrack until we get a vertex that meet the conditions.
        if graph[v.index(path[i-1])][v.index(vertex)] == 1 and vertex not in path:
            path[i]=vertex
            if hamiltonianPath(graph,v,path,i+1):
                return True
            path[i] = -1
    return False


# e=undirected_graph(e)
# graph = adjacencyMat(v, e)
# print(graph)
# path = [-1]*len(v)
# path[0]='Admin'
# # Here, the choice of start is not important, because if there is a
# # Hamiltonian cycle, there is no start and no end.
# print(hamiltonianCycle(graph, v, path, 1))
# print(path)