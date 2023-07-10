import psutil
import networkx as nx
from ProcessNode import ProcessNode


class ProcessGraph:

    def __init__(self):

        open('process_graph_output.txt', 'w+')

        self.labels = {}
        self.graph = nx.DiGraph()
        self.head = []

        process_tree = psutil.process_iter()
        process = next(process_tree)

        while process.ppid() == 0:
            print(process.name())
            #try:
            if process.pid != 0:
                head_node = self.createTree(process)
                self.head.append(head_node)

            #except psutil.NoSuchProcess:
             #   pass

            process = next(process_tree)

        #node = self.getNode('firefox')
        #node.printSubGraph()

    def createTree(self, node):

        process_node = ProcessNode(node)
        self.graph.add_node(process_node)
    #self.graph = nx.compose(self.graph, process_node.graph)
        self.labels[process_node] = process_node.name

        # print(process_node.process_string_repr())
        with open('process_graph_output.txt', 'a') as f:
            f.write(process_node.process_string_repr())

        for child in node.children():
            child_node = self.createTree(child)
            self.graph.add_edge(process_node, child_node)
            process_node.child_processes.append(child_node)

        return process_node

    def getNodeSizes(self):

        node_sizes = []

        for node in self.graph.nodes:
            if len(node.child_processes) > 10:
                node_sizes.append(20000)
            elif len(node.child_processes) > 5:
                node_sizes.append(10000)
            elif len(node.child_processes) > 1:
                node_sizes.append(5000)
            else:
                node_sizes.append(1000)

        return node_sizes

    def getNode(self, name):

        for node in self.graph:
            if node.name == name:
                return node

