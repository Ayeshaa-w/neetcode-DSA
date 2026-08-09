class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]
        for crs,pre in prerequisites:
            indegree[crs]+=1
            adj[pre].append(crs)
        q=collections.deque()
        res=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)  
        while q:
            node=q.popleft()
            res.append(node)
            for val in adj[node]:
                indegree[val]-=1
                if indegree[val]==0:
                    q.append(val)
        return res if len(res)==numCourses else []
