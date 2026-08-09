class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #khan's algorithm
        indegree=[0]*numCourses
        q=collections.deque()
        adjc=[[] for _ in range(numCourses)]#since *empty will not form seperat lists
        for adj,src in prerequisites:
            indegree[src]+=1
            adjc[adj].append(src)
        finish=0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            finish+=1
            for val in adjc[node]:
                indegree[val]-=1
                if indegree[val]==0:
                    q.append(val)
        return finish==numCourses

        
        