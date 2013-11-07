import random
import csv

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

    def add_node(self):
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

    def __str__(self):
        return 'Nodes: {0}\nEdges: {1}'.format(self.nodes, self.edges)