class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        while q :
            curr=q.popleft()
            completed_res+=1
            for connected in pre_list[curr]:
                count[connected]-=1
                if count[connected]==0:
                    q.append(connected)
        if completed_res==numCourses:
            return True
        return False




        