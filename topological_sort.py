# refer - https://www.interviewcake.com/concept/python3/topological-sort


def topological_sort(graph):
    indegrees = {n:0 for n in graph}
    for node in graph:
        for neighbour in graph[node]:
            indegrees[neighbour] += 1
    
    nodes_with_zero_indegrees = []
    for node in indegrees:
        if indegrees[node] == 0:
            nodes_with_zero_indegrees.append(node)
    
    topological_order = []
    
    while len(nodes_with_zero_indegrees)>0:
        
        node = nodes_with_zero_indegrees.pop()
        topological_order.append(node)
        
        for neighbour in graph[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                nodes_with_zero_indegrees.append(neighbour)
        
    if len(topological_order) == len(indegrees):
        print(topological_order)
        return 
    else:
        print("Cycle")
        return 


# Test
# a dictionary with node:adjacent nodes ie., the nodes it connect to i.e., it being the source
graph = {0:{1,2}, 1:{2,3}, 2:{4}, 3:{2,4}, 4:{}}
topological_sort(graph)
