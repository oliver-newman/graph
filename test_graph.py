#!/usr/bin/env python3
"""
Units tests for the graph module.
Author: Oliver Newman
Date: October 2016
"""

import unittest
from graph import Graph

VC = 100 # Default vertex count
VERTICES = list(range(VC))
EDGES = [((37 * i + 4597820) % VC, (31 * i + 6324957) % VC) for i in range(VC**2)]


class TestGraphMethods(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            self.assertTrue(graph.has_vertex(v))

    def test_remove_vertex(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            graph.remove_vertex(v)
            self.assertFalse(graph.has_vertex(v))

    def test_add_edge(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            for v in VERTICES:
                graph.add_edge(v, (v + 3) % len(VERTICES))
        for v in VERTICES:
            for v in VERTICES:
                self.assertTrue(graph.has_edge(v, (v + 3) % len(VERTICES)))


if __name__ == "__main__":
    unittest.main()
