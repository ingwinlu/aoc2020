from .task import build_graph, mybag, nx


def plot():
    import matplotlib.pyplot as plt
    plt.figure(figsize=(75, 75))
    G = build_graph()
    pos = nx.random_layout(G)

    # nodes
    otherbags = G.nodes() - mybag
    nx.draw_networkx_nodes(
        G, pos, nodelist=[mybag], node_color="red",
        alpha=1
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=otherbags, node_color="b",
        alpha=0.25
    )

    # edges
    nx.draw_networkx_edges(G, pos, alpha=0.25)

    # labels
    # nx.draw_networkx_labels(G, pos, G.nodes(), font_size=4)

    plt.savefig("Graph.png", format="PNG")


if __name__ == "__main__":
    plot()
