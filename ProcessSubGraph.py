from Node import Node
import networkx as nx
import matplotlib.pyplot as plt
import math
import inspect


class ProcessGraph:

    children = []
    names = {}

    def __init__(self, process):

        self.name = process.name()
        process_dict = process.as_dict()

        for key, value in process_dict.items():

            if value not in (None, '', [], {}):
                if isinstance(value, (int, str, float, list)):
                    node = Node(key, value)
                else:
                    node = Node(key, 'obj')
                    members = self.extract_object_members(value)
                    for k, v in members.items():
                        node.addChild(Node(k, v))

                self.children.append(node)

        #print(process_dict)

    def extract_object_members(self, obj):

        members = {}

        for key in dir(obj):
            if not key.startswith('_'):

                value = getattr(obj, key)
                if isinstance(value, (int, str, float)):
                    members[key] = value

        return members

    def getGraph(self):

        G = nx.DiGraph()
        G = self.addChildren(self, G)

        return G
    def addChildren(self, node, graph):

        print(node.name)
        graph.add_node(node)
        self.names[node] = node.name

        for child in node.children:
            graph.add_edge(node, child)
            graph = self.addChildren(child, graph)

        return graph

    def printGraph(self, graph):

        node_sizes = []

        for node in graph.nodes:
            if len(node.children) > 10:
                node_sizes.append(16000)
            elif len(node.children) > 5:
                node_sizes.append(8000)
            elif len(node.children) > 1:
                node_sizes.append(4000)
            else:
                node_sizes.append(2000)


        fig = plt.figure(figsize=(84, 84))
        pos = nx.spring_layout(graph, k=0.9, iterations=100)

        nx.draw_networkx_nodes(graph, pos, node_size=node_sizes, node_color='lightgray', edgecolors='black')
        nx.draw_networkx_edges(graph, pos, width=0.75)
        nx.draw_networkx_labels(graph, pos, labels=self.names, font_size=12)
        plt.show()

