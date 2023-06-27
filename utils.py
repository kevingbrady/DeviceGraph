import matplotlib.pyplot as plt
import networkx as nx
import psutil
import math
from ProcessSubGraph import ProcessGraph

count = 0
names = {}


def addChildren(node, graph):

    print(node.name)
    graph.add_node(node)
    names[node] = node.name

    for child in node.children:

        graph.add_edge(node, child)
        graph = addChildren(child, graph)

    return graph


if __name__ == '__main__':

    processes = psutil.process_iter()

    G = nx.DiGraph()
    addChildren.counter = 0

    for process in processes:

        if process.ppid() == 0:

            if process.pid != 0:

                try:
                    process_graph = ProcessGraph(process)
                    G = process_graph.getGraph()

                    print(G.nodes)
                    print('Nodes: %d' % (len(G.nodes)))
                    print('Edges: %d' % (len(G.edges)))

                    process_graph.printGraph(G)

                except psutil.NoSuchProcess:
                    pass

        break

    '''
    node_sizes = []

    for node in G.nodes:
        if len(node.children) > 10:
            node_sizes.append(20000)
        elif len(node.children) > 5:
            node_sizes.append(10000)
        elif len(node.children) > 1:
            node_sizes.append(5000)
        else:
            node_sizes.append(1000)

    pos = nx.spring_layout(G, k=5/math.sqrt(G.order()), iterations=50)
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightgray', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=0.75)
    nx.draw_networkx_labels(G, pos, labels=names, font_size=8)
    plt.show()
    '''