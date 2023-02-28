import random

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = {i: [] for i in range(size)}

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def generate_random_graph(self):
        for i in range(self.size):
            for j in range(i+1, self.size):
                if random.random() > 0.5:
                    self.add_edge(i, j, random.randint(0, 9))


    def print_graph(self):
        for i in range(self.size):
            print(i, ": ", end="")
            for j in self.graph[i]:
                print(f"({j[0]}, {j[1]}) ", end="")
            print()


