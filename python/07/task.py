import networkx as nx


mybag = 'shiny gold'


def build_graph():
    graph = nx.DiGraph()
    for line in open('input.txt'):
        words = iter(line.split())

        def take_color():
            color = ' '.join([next(words), next(words)])
            # print(color)
            return color
        # drab tomato bags contain no other bags.
        bb = take_color()
        graph.add_node(bb)
        _ = next(words)   # 3 -> bag(s)
        _ = next(words)  # 4 -> contain
        while True:
            quanti = next(words)  # 5 -> quanti
            if quanti == "no":
                break
            child = take_color()
            graph.add_edge(bb, child, weight=int(quanti))
            bag = next(words)  # bag(s)[,.]
            if bag.endswith('.'):
                break

    return graph


def task1():
    g = build_graph()
    return len(nx.algorithms.dag.ancestors(g, mybag))


def get_child_weight(g, node):
    w = 1
    for s in g[node]:
        w += g[node][s]['weight'] * get_child_weight(g, s)
    return w


def task2():
    g = build_graph()
    w = get_child_weight(g, mybag) - 1
    return w


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
