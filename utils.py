import matplotlib.pyplot as plt
import networkx as nx
import psutil
import math
from ProcessNode import ProcessNode
from ProcessGraph import ProcessGraph

def addNode(node, graph, labels):

    process_node = ProcessNode(node)
    graph.add_node(process_node)
    labels[process_node] = process_node.name

    #print(process_node.process_string_repr())
    with open('process_graph_output.txt', 'a') as f:
        f.write(process_node.process_string_repr())

    for child in node.children():
        child_node, graph, labels = addNode(child, graph, labels)
        graph.add_edge(process_node, child_node)

    return process_node, graph, labels


if __name__ == '__main__':

    process_graph = ProcessGraph()
    G = process_graph.graph

    print('Nodes: %d' % (len(G.nodes)))
    print('Edges: %d' % (len(G.edges)))

    fig = plt.figure(figsize=(84, 84))
    pos = nx.spring_layout(G, k=0.75, iterations=100)

    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightgray', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=0.75)
    nx.draw_networkx_labels(G, pos, labels=process_graph.labels, font_size=12)
    plt.show()
