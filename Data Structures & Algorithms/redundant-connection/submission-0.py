class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        p=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(n):
            P=p[n]
            while P!=p[P]:
                p[P]=p[p[P]]
                P=p[P]
            return P

        def union(n1,n2):
            root_n1=find(n1)
            root_n2=find(n2)
            if root_n1 == root_n2:
                return False
            if p[root_n1]>p[root_n2]:
                p[root_n2]=p[root_n1]
                rank[root_n1]+=rank[root_n2]
            else:
                p[root_n1]=p[root_n2]
                rank[root_n2]+=rank[root_n1]
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        