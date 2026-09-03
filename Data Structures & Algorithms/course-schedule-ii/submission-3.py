class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_list={i:[] for i in range(numCourses)}
        count=[0]*numCourses
        for crs,pre in prerequisites:
            pre_list[pre].append(crs)
            count[crs]+=1
        q=collections.deque()
        for crs in range(numCourses):
            if count[crs]==0:
                q.append(crs)
        completed_res=0
        res=[]
        while q :
            curr=q.popleft()
            res.append(curr)
            completed_res+=1
            for connected in pre_list[curr]:
                count[connected]-=1
                if count[connected]==0:
                    q.append(connected)
        if completed_res==numCourses:
            return res
        return []



        