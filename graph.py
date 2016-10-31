"""
Graph implementation in Python.
Author: Oliver Newman
Date: October 2016
"""

class Graph(object):
    """Implementation of an adjacency-list directed graph.

    Attributes:
        vertices: A dict mapping a vertex to a set of vertices to which that
            vertex is connected with an edge.
    """
    def __init__(self, vertices = [], edges = []):
        """Initializes a graph.

        Args:
            vertices: An optional list of edges with which to initialize the
                graph.
            edges: An optional list of edges (2-tuples of the form (start, end))
                with which to initialize the graph.
        """
        self.vertices = {}
        for v in vertices:
            self.add_vertex(v)
        for e in edges:
            self.add_edge(e[0], e[1])

    def __str__(self):
        """Returns a string representation of the Graph.

        Returns:
            The string representation of the Graph's vertices dict.
        """
        result = "{"
        num_vertices = len(self.vertices)
        for v in self.vertices:
            result += "{}->{}, ".format(v, list(self.vertices[v]))
        result += "\b\b}"
        return result

    __repr__ = __str__

    @property
    def edges(self):
        """Returns a list of edges as 2-tuples of the form (start, end)."""
        edges = []
        for v1 in self.vertices:
            for v2 in self.vertices[v1]:
                edges.append((v1, v2))
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

    def num_edges(self):
        """Returns the number of edges in the graph."""
        num_edges = 0
        for edges in self.vertices.values():
            num_edges += len(edges)

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

    def out_edges(self, vertex):
        """Returns a list of the outgoing edges from a vertex."""
        return list(self.vertices[vertex])

    def in_edges(self, vertex):
        """Returns a list of the incoming edges to a vertex."""
        return [v for v in self.vertices if vertex in self.vertices[v]]

    # def is_reachable(self, start, end):
