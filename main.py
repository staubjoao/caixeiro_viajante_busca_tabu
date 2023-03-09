import networkx as nx
import random

# Gera uma solução inicial aleatória


def initial_solution(g):
    nodes = list(g.nodes())
    random.shuffle(nodes)
    return nodes

# Gera todos os vizinhos da solução atual


def neighborhood_func(s):
    neighborhoods = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            n = s.copy()
            n[i], n[j] = n[j], n[i]
            neighborhoods.append(n)
    return neighborhoods

# Critério de aspiração


def aspiration_criterion(s):
    return False

# Critério de parada


def stopping_criterion(iteration, s):
    return iteration >= 500

# Calcula o custo da solução


def cost(g, s):
    c = 0
    for i in range(len(s)):
        c += g[s[i]][s[(i + 1) % len(s)]]['weight']
    return c


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[None] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest, weight):
        self.matrix[src][dest] = weight
        self.matrix[dest][src] = weight

    def get_weight(self, src, dest):
        return self.matrix[src][dest]


def generate_random_tour(graph):
    tour = list(range(graph.num_vertices))
    random.shuffle(tour)
    return tour


def calculate_tour_length(graph, tour):
    tour_length = 0
    for i in range(len(tour)):
        src, dest = tour[i], tour[(i+1) % len(tour)]
        tour_length += graph.get_weight(src, dest)
    return tour_length


def get_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i+1, len(tour)):
            neighbor = tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors


def tabu_search(initial_solution, neighborhood_func, aspiration_criterion, stopping_criterion, tabu_size):
    s_curr = initial_solution
    best_solution = initial_solution
    tabu_list = []
    iter = 0

    while not stopping_criterion(iter, s_curr):
        iter += 1
        s_best = None
        for s in neighborhood_func(s_curr):
            if s not in tabu_list or aspiration_criterion(s):
                if s_best is None or s < s_best:
                    s_best = s
        if s_best is None:
            break
        s_curr = s_best
        if s_curr < best_solution:
            best_solution = s_curr
        tabu_list += [s_best]
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution


# Exemplo de uso
g = Graph(50)
with open("grafo.txt", "r") as f:
    for line in f:
        values = list(map(int, line.split(" ")))
        g.add_edge(values[0], values[1], values[2])


print("teste")
best_tour, best_length = tabu_search(g, max_iterations=500, tabu_size=20)
print("Melhor caminho encontrado:", best_tour)
print("Comprimento do caminho:", best_length)
