# https://youtu.be/U196c9aQq5c

def get_adjs_lsit(num_nodes, from_list, to_list): # Getting the adjacent list i.e., the graph
    adj_list = [[] for _ in range (num_nodes+1)]
    
    for u, v in zip(from_list, to_list):
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list

# at - Current node that i am at
# parent - cource of my current node (used to eliminate bidirectional cycles)
# partial - array that stores path up to this point(also used to check cycle size)
# adj_list - graph
# visited - boolean array for nodes 


def visit(at, parent, partial, adj_list, visited, all_trios):
    pass

def get_cycles(num_nodes, from_list, to_list):
    adj_list = get_adjs_lsit(num_nodes, from_list, to_list)
    print(adj_list)
    
    visited = [False]* (num_nodes+1)
    al_trios = []
    
    for node in range(1,num_nodes+1):
        if not visited[node]:
            visit(node,-1,[],adj_list, visited, all_trios)
            pass
    
    print("all trios",al_trios)



from_list = [1,2,2,3,4,5]
to_list = [2,4,5,5,5,6]
num_nodes = 6
get_cycles(num_nodes, from_list, to_list)
