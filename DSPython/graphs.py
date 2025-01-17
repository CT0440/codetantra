#dfs
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def dfs(g,root):
    visited=set()
    stack=[]
    visited.add(root)
    stack.append(root)
    while stack:
        s=stack.pop()
        print(s,end="-->")
        for i in reversed(graph[s]):        
            
            if i is not visited:
                visited.add(i)
                stack.append(i)
    print("None")

dfs(graph,'A')

#bfs
from collections import deque

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def bfs(g,root):
    visited=set()
    queue=deque()
    visited.add(root)
    queue.append(root)
    while queue:
        s=queue.popleft()
        print(s,end="-->")
        for i in graph[s]:
            if i is not visited:
                visited.add(i)
                queue.append(i)
    print("None")

bfs(graph,'A')

class Graph:
    def __init__(self):
        # Dictionary to store the graph (adjacency list)
        self.graph = {}

    def add_node(self, node):
        """Add a new node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, bidirectional=True):
        """Add an edge between node1 and node2. Bidirectional by default."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        
        # Add the edge
        self.graph[node1].append(node2)
        if bidirectional:
            self.graph[node2].append(node1)

    def display(self):
        """Print the adjacency list of the graph."""
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(map(str, neighbors))}")

    def bfs(self, start):
        """Breadth-First Search (BFS)"""
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start, visited=None):
        """Depth-First Search (DFS)"""
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    print("Graph Representation:")
    g.display()

    print("\nBFS Traversal:")
    g.bfs(1)

    print("\n\nDFS Traversal:")
    g.dfs(1)