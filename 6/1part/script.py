from collections import defaultdict

def addEdge(graph, u, v):
    graph[u].append(v)


def generate_edges(graph):
    edges = []

    for node in graph:

        for neighbour in graph[node]:

            edges.append((node, neighbour))

    return edges


def find_path(graph, start, end, path =[]):

    path += [start]
    if start == end:
        return path
    for node in graph[start]:
        print(f'outnode: {node} path: {path}')
        if node not in path:
            print(f'node: {node}')
            newpath = find_path(graph, node, end, path)
            print(f'Npath: from {node} {end} {newpath}')
            if newpath:
#                path = []
                return newpath
            else:
                path.remove(node)
    return None

def find_total_orbits(graph, edges):
    totalOrbits = 0
    for edge in edges:
#        print(edge[0])
#        if edge[0] != 'COM':
        rpath = find_path(graph, edge[0], 'COM',[])
#        print(rpath)
        if rpath:
            totalOrbits += len(rpath)-1
    return totalOrbits


def find_orbits_bet(graph, node1, node2):
    totalOrbits = 0
#    for edge in edges:
#        print(edge[0])
#        if edge[0] != 'COM':
    rpath = find_path(graph, node1, node2,[])
    print(rpath)
    if rpath:
        totalOrbits += len(rpath)-3
    return totalOrbits


def main():
    graph = defaultdict(list)

    f = open('input.txt','r')
    nodelist = [ x.rstrip() for x in f]
    for node in nodelist:
        pair = node.split(')')
        addEdge(graph, pair[0], pair[1])
        addEdge(graph, pair[1], pair[0])
    edges = generate_edges(graph)
    print(graph)
    print(edges)
#    print(find_total_orbits(graph, edges))
    print(find_orbits_bet(graph,'YOU','SAN'))

if __name__ == "__main__":
    main()
