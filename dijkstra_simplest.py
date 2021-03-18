class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = [[0 for col in range(v)] for row in range(v)]
    
    def print_sol(self, dist):
        print("vertex \t from source")
        for node in range(self.v):
            print(node," \t ",dist[node])
    
    def get_min_dist(self, dist, visited):
        min_dist=float('inf')
        for v in range(self.v):
            if dist[v]<min_dist and visited[v]==False:
                min_dist = dist[v]
                min_index = v
        return min_index
    
    def dijkstra(self, src):
        dist = [float('inf')]*self.v
        visited = [False]*self.v
        
        dist[src]=0
        
        for nodes in range(self.v):
            min_index = self.get_min_dist(dist, visited)
            visited[min_index] = True
            for j in range(self.v):
                if self.graph[min_index][j]>0 and visited[j]==False and dist[j]>dist[min_index]+self.graph[min_index][j]:
                    dist[j]=dist[min_index]+self.graph[min_index][j]
        
        self.print_sol(dist)



# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0); 
            
