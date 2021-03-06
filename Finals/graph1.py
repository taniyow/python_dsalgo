from collections import defaultdict
 
# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
 
# definition of function
def generate_edges(graph):
    edges = []
    
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
 
# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print(generate_edges(graph))
