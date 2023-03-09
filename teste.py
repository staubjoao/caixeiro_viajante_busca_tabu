import random

with open("grafo.txt", "w") as f:
    num_vertices = 50
    num_arestas = 100  # número de arestas a serem geradas
    for i in range(num_arestas):
        v1 = random.randint(0, num_vertices-1)
        v2 = random.randint(0, num_vertices-1)
        while v1 == v2:
            v2 = random.randint(0, num_vertices-1)
        weight = random.randint(1, 100)
        line = f"{v1} {v2} {weight}"
        f.write(line + "\n")
