class Dijkastra:
    def __init__(self,relations):
        self.relations = relations

    def s_path(self , start = None):
        # first we make the adgency list
        # ui : [[vi,wi],[vi + 1 , wi + 1]]

        # we will let the start be automatically be the lexigraphical start ie "a"
        import collections
        adj = collections.defaultdict(list)
        nodes = set()

        for u , v , w in self.relations:
            nodes.add(u)
            nodes.add(v)
            if [v,w] not in adj[u]:
                adj[u].append([v,w]) # avoid duplicates

        if start == None:
            start = list(sorted(nodes))[0] # always start at first letter
        else:
            if start not in nodes:
                raise ValueError("invalid start")
        seen = list()
        def dfs(edge): # iteratively checking
            if not adj[edge]:
                seen.append(edge)
                return seen
            else:
                seen.append(edge)
                optimum = min(adj[edge])[0]
                if optimum not in seen:
                    return dfs(optimum)               
        return dfs(start)
            
                
        

 ### takes set of relations of the form {u , v , w}

p = [["e","g",1],["d","g",2],["a","d",1],["b","a",8],["c","b",7],["f","g",3],["f","c",1]]


f = Dijkastra(relations = p)
              
print(f.s_path())




