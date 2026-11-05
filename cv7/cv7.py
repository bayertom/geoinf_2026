#Graph definition
G = {
     1:[2, 3, 5],
     2:[1, 3, 4, 7, 8],
     3:[1, 2, 6, 7],
     4:[2, 9],
     5:[1, 6],
     6:[3, 5, 7, 8, 9],
     7:[2, 3, 6, 8],
     8:[2, 6, 7, 9],
     9:[4, 6, 8]
      }

#Coordinates X, Y
C = {
    1 : [95, 322],
    2 : [272, 331],
    3 : [173, 298],
    4 : [361, 299],
    5 : [82, 242],
    6 : [163, 211],
    7 : [244, 234],
    8 : [333, 225],
    9 : [412, 196]
}

#BFS

def BFS(G, start):
    #Number of nodes
    n = len(G)
    
    #Suplementary data structures
    s = ["N"] * (n + 1) 
    p = [None] * (n + 1)
    
    #Create Query
    Q = []

    #Add start point to the queue
    Q.append(start)
    
    #Open start node
    #s[start] = "O"
    

    #Repeat until Q is empty
    while Q:

        #Take first node
        u = Q.pop(0)
        
        #Change status to open
        #s[u] = "O"
        
        #Browse its neighbors
        for v in G[u]:
            
            #Is node new?
            if s[v] == 'N':
                #Change status to open 
                s[v] = "O"
                
                #Change predecessor
                p[v] = u

                #Add v to Q
                Q.append(v)
                
        #Close u
        s[u] = "C"
    
    return p

def rec(p, u, v):
    #Back recontruction, path shortenning
    path = []
    
    #Repeat until v == u
    while v != u:
        
        #Add node
        path.append(v)
        
        #Go to predecessor
        v = p[v] 
        
    #Add first node of the path
    path.append(u)
    
    return path

    


#Call BFS
start = 1
p = BFS(G, start)
print(p)

#PAth reconstruction
end = 9
path = rec(p, start, end)

print(path)


