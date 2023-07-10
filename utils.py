from ProcessGraph import ProcessGraph


if __name__ == '__main__':

    process_graph = ProcessGraph()
    G = process_graph.graph

    print('Nodes: %d' % (len(G.nodes)))
    print('Edges: %d' % (len(G.edges)))

    '''
    fig = plt.figure(figsize=(84, 84))
    pos = nx.spring_layout(G, k=0.75, iterations=100)

    nx.draw_networkx_nodes(G, pos, node_size=process_graph.getNodeSizes(), node_color='lightgray', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=0.75)
    nx.draw_networkx_labels(G, pos, labels=process_graph.labels, font_size=12)
    plt.show()
    '''