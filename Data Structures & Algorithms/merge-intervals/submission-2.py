class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dp=defaultdict(int)
        for start,end in intervals:
            dp[start]+=1
            dp[end]-=1
        interval=[]
        res=[]
        have=0
        for i in sorted(dp):
            if not interval:
                interval.append(i)
            have+=dp[i]
            if have==0:
                interval.append(i)
                res.append(interval)
                interval=[]
        return res



        