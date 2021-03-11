# https://youtu.be/U196c9aQq5c

def get_adjs_lsit(num_nodes, from_list, to_list): # Getting the adjacent list i.e., the graph
    adj_list = [[] for _ in range (num_nodes+1)]
    
    for u, v in zip(from_list, to_list):
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list



def get_cycles(num_nodes, from_list, to_list):
    adj_list = get_adjs_lsit(num_nodes, from_list, to_list)
    print(adj_list)



from_list = [1, 1, 2, 2, 3, 4]
to_list = [2, 3, 3, 4, 4, 5]
num_nodes = 5
get_cycles(num_nodes, from_list, to_list)
