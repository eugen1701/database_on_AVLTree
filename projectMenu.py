from Include.try2 import *
from Include.step2 import *
from Include.step3 import *
from Include.step4 import *

class Project:
    def __init__(self):
        """
        This class is managing the all steps of the project. Its role is to print the menu and to let the user
        choose what step to see running
        """
        self.menu = "Press one of the following numbers:\n1. Step 1(The ranked game)\n2. Step 2(Who is the killer?)" \
                    "\n3. Step 3(The shortest path between rooms) \n4. Step 4(The path of all rooms)"
        self.function = {'1':self.step1calling, '2':self.step2calling, '3':self.step3calling, '4':self.step4calling}
    def step1calling(self):
        tree = None
        game = Game(tree)
        game.start()
    def step2calling(self):
        menu_step2 = "1. Graph coloring(first try, doesn't work)\n2. Brute force (working algorithm)\n0. Exit step 2"
        while True:
            print(menu_step2)
            command = input("Command step 2: >>> ")
            if command == "1":
                print("\n[Graph coloring] For each vertex, we will color it depending on the colors of its neighbors :\n")
                graph_coloring(v_step2, e_step2, 3)
            elif command == "2":
                print("\n[Brute Force] Here are all the possible pairs of impostors :\n")
                print(brute_force(e_step2))
            elif command == "0":
                break
            else:
                print("Error. Try again!")
    def step3calling(self):
        print("\n\n\n************************Crewmates************************\n\n")
        graph = v_step3, e_step3
        floyd_warshall(graph)
        print("\n\n\n************************Impostors************************\n\n")
        graph = v_step3, e_step3_imp
        floyd_warshall(graph)
    def step4calling(self):
        e = undirected_graph(e_step4)
        graph = adjacencyMat(v_step4, e)
        #print(graph)
        path = [-1] * len(v_step4)
        path[0] = 'Admin'
        hamiltonianPath(graph, v_step4, path, 1)
        print(path)
    def showMenu(self):
        while True:
            try:
                print(self.menu)
                command = input("Select a step: >>> ")
                if command in self.function.keys():
                    self.function[command]()
                elif command =='exit':
                    break
                else:
                    raise ValueError()
            except Exception as e:
                print("Something went wrong. Try again!")
                print(e)

project = Project()
project.showMenu()