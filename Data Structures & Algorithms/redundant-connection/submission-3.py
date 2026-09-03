class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        def solve(source,target,visited):
            if source==target:
                return True
            visited.add(source)
            for neighbours in adj[source]:
                if neighbours not in visited:
                    if solve(neighbours,target,visited):
                        return True
            return False

        for u,v in edges:
            visited=set()
            if u in adj and v in adj and solve(u,v,visited):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
