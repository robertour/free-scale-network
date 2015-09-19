import random
import csv

import networkx as nx
import matplotlib.pyplot as plt

def weighted_random(weights):
    number = random.random() * sum(weights.values())
    for k,v in weights.items():
        if number < v:
            break
        number -= v
    return k


class FreeScaleNetwork(object):

    nodes = 0
    edges = []

    def add_node(self, nodes=1):
        for i in range(nodes):
            current_node = self.nodes + 1
            if self.nodes == 1:
                self.edges.append((current_node, 1))
            elif self.nodes > 1:
                probabilities = self.calculate_probability()
                first_node = weighted_random(probabilities)
                del probabilities[first_node]
                second_node = weighted_random(probabilities)
                self.edges.append((current_node, first_node))
                self.edges.append((current_node, second_node))
            self.nodes = current_node

    def calculate_probability(self):
        degrees = {}
        total = 0
        for edge in self.edges:
            for i in edge:
                total = total + 1
                if not i in degrees:
                    degrees[i] = 1
                else:
                    degrees[i] = degrees[i] + 1
        probabilities = {}
        for n, i in degrees.items():
            probabilities[n] = i / total
        return probabilities

    def nodes_to_csv(self, filename):
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Id"])
            for i in range(1, self.nodes + 1):
                writer.writerow([i])

    def edges_to_csv(self, filename):
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Source", "Targe"])
            for edge in self.edges:
                writer.writerow([edge[0], edge[1]])

    def add_nodes_and_edges(self, graph):
        for node in range(self.nodes):
            graph.add_node(node)

        for edge in self.edges:
            graph.add_edge(edge[0], edge[1])

    def draw_centralized(self):
        graph = nx.Graph()

        self.add_nodes_and_edges(graph)

        pos = nx.shell_layout(graph)
        nx.draw(graph, pos)

        plt.show()

    def draw_random(self):
        graph = nx.random_geometric_graph(200,0.125)

        self.add_nodes_and_edges(graph)

        pos = nx.get_node_attributes(graph, 'pos')

        nx.draw(graph, pos)

        plt.xlim(-0.05,1.05)
        plt.ylim(-0.05,1.05)
        plt.axis('off')
        plt.show()

    def __str__(self):
        return 'Nodes: {0}\nEdges: {1}'.format(self.nodes, self.edges)
    
    def draw_other(self):
        graph = nx.Graph()

        self.add_nodes_and_edges(graph)

        pos = nx.spectral_layout(graph)
        nx.draw(graph, pos)

        plt.show()