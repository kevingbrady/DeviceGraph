from Node import Node
import networkx as nx
import matplotlib.pyplot as plt
import math
import inspect


class ProcessNode:

    children = []
    child_processes = []
    names = {}

    def __init__(self, process):

        self.name = process.name()
        self.graph = nx.DiGraph()

        process_dict = process.as_dict()

        for key, value in process_dict.items():

            if value not in (None, '', [], {}):
                if isinstance(value, (int, str, float, list)):
                    node = Node(key, value)
                else:
                    node = Node(key, 'obj')
                    members = self._extract_object_members(value)
                    for k, v in members.items():
                        node.addChild(Node(k, v))

                self.children.append(node)

        #self._generateSubGraph()

    def _extract_object_members(self, obj):

        members = {}

        for key in dir(obj):
            if not key.startswith('_'):

                value = getattr(obj, key)
                if isinstance(value, (int, str, float)):
                    members[key] = value

        return members

    def _generateSubGraph(self):

        self.graph = self.addChildren(self)

    def addChildren(self, node):

        #print(node.name)
        self.graph.add_node(node)
        self.names[node] = node.name

        for child in node.children:
            self.graph.add_edge(node, child)
            self.graph = self.addChildren(child)

        return self.graph

    def getValue(self, name):
        for node in self.children:
            if node.name == name:
                return node.value

    def printSubGraph(self):

        node_sizes = []

        for node in self.graph.nodes:
            if type(node) is ProcessNode:
                node_sizes.append(16000)
            elif len(node.children) > 5:
                node_sizes.append(8000)
            elif len(node.children) > 3:
                node_sizes.append(4000)
            else:
                node_sizes.append(2000)


        fig = plt.figure(figsize=(84, 84))
        pos = nx.spring_layout(self.graph, k=0.75, iterations=100)

        nx.draw_networkx_nodes(self.graph, pos, node_size=node_sizes, node_color='lightgray', edgecolors='black')
        nx.draw_networkx_edges(self.graph, pos, width=0.75)
        nx.draw_networkx_labels(self.graph, pos, labels=self.names, font_size=12)
        plt.show()

    def process_string_repr(self):
        processString = f'{self.name}: [\n'
        for child in self.children:
            processString += '\t\t' + child.node_string_repr() + '\n'

        processString += ']\n'

        return processString

    def __repr__(self):
        return f'{self.name}'