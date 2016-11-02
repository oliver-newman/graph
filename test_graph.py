#!/usr/bin/env python3
"""
Unit tests for the directed graph module.
Author: Oliver Newman
Date: October 2016
"""

import unittest
from graph import Directed_Graph

VC = 100 # Default vertex count
VERTICES = list(range(VC))
EDGES = [((37 * i + 45978) % VC, (31 * i + 63249) % VC) for i in range(VC**2)]
with open('state_borders.txt', 'r') as border_file:
    STATE_BORDERS = [border.strip("\n").split(" ") for border in border_file.readlines()]
    border_file.close()


class TestGraphMethods(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            self.assertTrue(graph.has_vertex(v))
        self.assertEqual(graph.num_vertices(), len(VERTICES))

    def test_remove_vertex(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            graph.remove_vertex(v)
            self.assertFalse(graph.has_vertex(v))
        self.assertEqual(graph.num_vertices(), 0)

    def test_add_edge(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            dest1 = (v + 3) % len(VERTICES)
            dest2 = (v + 8) % len(VERTICES)
            graph.add_edge(v, dest1)
            graph.add_edge(v, dest2)
            graph.add_edge(dest1, v)
            graph.add_edge(dest2, v)
        for v in VERTICES:
            dest1 = (v + 3) % len(VERTICES)
            dest2 = (v + 8) % len(VERTICES)
            self.assertTrue(graph.has_edge(v, dest1))
            self.assertTrue(graph.has_edge(v, dest2))
        self.assertEqual(graph.num_edges(), 4 * len(VERTICES))

    def test_shortest_path(self):
        graph = Graph(VERTICES)
        for v in VERTICES:
            dest1 = (v + 3) % len(VERTICES)
            dest2 = (v + 8) % len(VERTICES)
            graph.add_edge(v, dest1)
            graph.add_edge(v, dest2)
            # graph.add_edge(dest1, v)
            # graph.add_edge(dest2, v)
        for v in VERTICES:
            print(graph.shortest_path(v, VERTICES[0]))
    
    def test_states(self):
        graph = Graph()
        for border in STATE_BORDERS:
            for state in border:
                try:
                    graph.add_vertex(state)
                except ValueError:
                    pass
            graph.add_edge(*border)
            graph.add_edge(*reversed(border))
        print(graph.shortest_path("ME", "CA"))


if __name__ == "__main__":
    unittest.main()
