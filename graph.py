"""
Graph implementation in Python.
Author: Oliver Newman
Date: October 2016
"""
from collections import deque

class Directed_Graph(object):
    """Implementation of an adjacency-list directed graph.

    Attributes:
        vertices: A dict mapping a vertex to a set of vertices to which that
            vertex is connected with an edge.
    """
    def __init__(self, vertices=None, edges=None):
        """Initializes a graph.

        Args:
            vertices: An optional list of edges with which to initialize the
                graph.
            edges: An optional list of edges (2-tuples of the form (start, end))
                with which to initialize the graph.
        """
        self.vertices = {}
        if vertices is None:
            return
        for vert in vertices:
            self.add_vertex(vert)

        if edges is None:
            return
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def __str__(self):
        """Returns a string representation of the Graph.

        Returns:
            The string representation of the Graph's vertices dict.
        """
        num_vertices = len(self.vertices)
        result = "{"

        for i, vertex in enumerate(self.vertices):
            result += "{}->{}".format(vertex, list(self.vertices[vertex]))
            if i != num_vertices - 1:
                result += ",\n"

        result += "}"
        return result

    __repr__ = __str__

    @property
    def edges(self):
        """Returns a list of edges as 2-tuples of the form (start, end)."""
        edges = []
        for start in self.vertices:
            for end in self.vertices[start]:
                edges.append((start, end))
        return edges

    def add_vertex(self, vertex):
        """Adds a vertex to the graph."""
        if vertex not in self.vertices:
            # Insert vertex with empty edge set
            self.vertices[vertex] = set()
        else:
            raise ValueError("Duplicate vertex names are not allowed.")

    def add_edge(self, start, end):
        """Adds an edge from vertex start to vertex end.

        Raises:
            KeyError if vertex named start or end does not exist.
        """
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
        else:
            raise KeyError("Can't attach edge to nonexistent vertex.")

    def num_vertices(self):
        """Returns the number of vertices in the graph."""
        return len(self.vertices)

    def num_edges(self):
        """Returns the number of edges in the graph."""
        num_edges = 0
        for edges in self.vertices.values():
            num_edges += len(edges)
        return num_edges

    def has_vertex(self, vertex):
        """Returns whether or not a vertex exists with the given name."""
        return vertex in self.vertices

    def has_edge(self, start, end):
        """Returns whether or not an edge exists from start to end."""
        return end in self.vertices[start]

    def remove_vertex(self, vertex):
        """Removes a vertex from the graph."""
        del self.vertices[vertex]
        for edges in self.vertices.values():
            edges.discard(vertex) # Try to remove incoming edge

    def remove_edge(self, start, end):
        """Removes an edge from the graph."""
        self.vertices[start].remove(end)

    def children(self, vertex):
        """Returns a list of the outgoing edges from a vertex."""
        return list(self.vertices[vertex])

    def parents(self, vertex):
        """Returns a list of the incoming edges to a vertex."""
        return [v for v in self.vertices if vertex in self.vertices[v]]

    def shortest_path(self, start, end):
        distance = {}
        parent = {}
        queue = deque()
        for vertex in self.vertices:
            distance[vertex] = -1
            parent[vertex] = None

        queue.appendleft(start)
        distance[start] = 0
        while len(queue):
            curr = queue.pop()
            if curr == end: # Found end vertex
                path = [curr]
                while parent[curr]:
                    curr = parent[curr]
                    path.insert(0, curr)
                return path
            for child in self.children(curr):
                if distance[child] < 0:
                    queue.appendleft(child)
                    parent[child] = curr
                    distance[child] = distance[curr] + 1 
        return None

    def is_reachable(self, start, end):
        return bool(self.shortest_path(start, end))
    






















