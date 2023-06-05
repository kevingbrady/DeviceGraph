import matplotlib.pyplot as plt
import networkx as nx
import psutil


def addChildren(node, graph):

    info = node.as_dict()

    for child in node.children():

        if node.name() == 'Google Chrome':

            graph.add_edges_from([(f'{node.pid}:{node.name()}', f'{child.pid}:{child.name()}')])

        if child.children():
            graph = addChildren(child, graph)

    return graph


if __name__ == '__main__':

    processes = psutil.process_iter()

    G = nx.DiGraph()

    for process in processes:

        if process.ppid() == 0:
            #G.add_node(f'{process.pid}:{process.name()}')

            if process.pid != 0:

                try:

                    G = addChildren(process, G)
                except psutil.NoSuchProcess:
                    pass

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap='jet', node_size=400)
    nx.draw_networkx_edges(G, pos, arrows=True)
    nx.draw_networkx_labels(G, pos)
    plt.show()