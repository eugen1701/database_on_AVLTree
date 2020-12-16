# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:42:24 2020

@author: 33610
"""

# Defining the data :
v_step2 = [0,1,2,3,4,5,6,7,8,9]
colored = []
e_step2 = [(0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),(3,8),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9)]
col = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

# Method to return a solution of the graph coloring problem
# considering a graph and the chromatic number : k (here 3)
def graph_coloring(v_step2, e_step2, k):
    # for each vertex, get all its neghbors
    for vertex in range(0,10):
        colneighbors=[]
        neighbors=[]
        for edge in e_step2:
            if vertex in edge:
                v1,v2 = edge
                if v1 == vertex:
                    neighbor = v2
                else:
                    neighbor = v1
                neighbors.append(neighbor)
                colneighbors.append(col[neighbor])
        print("vertex: "+str(vertex))
        print("neighbors: "+str(neighbors))
        print("colors of neighbors: "+ str(colneighbors))
        # for each of its neighbors, color it
        # if its not colored yet
        # and with a color that is not already taken
        for neighbor in neighbors:
            for color in range(0,k):
                if color not in colneighbors and vertex not in colored:
                    col[vertex] = color
                    colored.append(vertex)
                    print("colors of vertices: " + str(col))
    return col

# print(graph_coloring(v,e,3))
# print(v)


# Method to return the list of possible couples
# of imposotors considering the contraints :
# - 2 impostors : two for loops
def brute_force(e_step2):
    impostors=[]
    # - 1 impostor is 1, 4 or 5
    for i in [1,4,5]:
        for j in range(1,10):
            # - impostors cannot be the same person
            if i != j:
                # - they never had seen each other
                if (i,j) not in e_step2 and (j,i) not in e_step2:
                    if (i,j) not in impostors and (j,i) not in impostors:
                        impostors.append((i,j))
    return impostors
# print(brute_force(e))