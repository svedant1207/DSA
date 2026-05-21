from collections import deque
class GraphMatrix:
    def __init__(self, vertices):
        self.v = vertices
        self.matrix = [[0]*vertices for v in range(vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def has_edge(self, u, v):
        return self.matrix[u][v] == 1 or self.matrix[v][u] == 1

    def print_edge(self):
        for row in self.matrix:
            print(row)

    # traversal
    def bfs(self, start):
        visited = [False] * self.v
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nb in range(self.v):
                if self.matrix[node][nb] == 1 and not visited[nb]:
                    visited[nb] = True
                    queue.append(nb)

        return order

    def dfs(self, start):
        visited = [False] * self.v
        stk = [start]
        visited[start] = True
        order = []

        while stk:
            node = stk.pop()
            order.append(node)

            for nb in range(self.v):
                if self.matrix[node][nb] == 1 and not visited[nb]:
                    visited[nb] = True
                    stk.append(nb)
        return order


# matrix
g = GraphMatrix(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(2,3)

g.print_edge()

class Graph:
    def __init__(self):
        self.list = {}

    def add_vertex(self, v):

        if v not in self.list:
            self.list[v] = []

    def add_edge(self, v, u):
        if v in self.list and u in self.list:
            self.list[v].append(u)
            self.list[u].append(v)

    def neighbours(self, v):
        return self.list.get(v, [])

    def p(self):
        for v, e in self.list.items():
            print(f'This vertex has {v} vertex and {e} edges')

    def __str__(self):
        return '\n'.join(f"{v}:{neighbour}" for v,neighbour in self.list.items())

    # traversal

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nb in self.list[node]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)

        return order

    def dfs(self, start):
        visited = set()
        stk = [start]
        order = []

        while stk:
            node = stk.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)

            for nb in self.list[node]:
                if nb not in visited:
                    stk.append(nb)
        return order

#list

g1 = Graph()

g1.add_vertex(0)
g1.add_vertex(1)
g1.add_vertex(2)
g1.add_vertex(3)

g1.add_edge(0,1)
g1.add_edge(0,2)
g1.add_edge(0,3)
g1.add_edge(1,3)
g1.add_edge(1,2)
g1.add_edge(2,3)

g1.neighbours(0)
g1.neighbours(1)
g1.neighbours(2)
g1.neighbours(3)
g1.p()
print(g1.__str__())

