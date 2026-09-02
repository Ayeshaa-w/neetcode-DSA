def minimize_max_segment_sum(N,K,A):
    #greedy approach
    def cansplit(limit_mid):
        segments=0
        currentsum=0
        for num in A:
            currentsum+=num
            if currentsum>limit_mid:
                segments+=1
                currentsum=num
        return segments+1<=K
    l,r=max(A),sum(A)
    res=r
    while l<=r:
        mid=l+((r-l)//2)
        if cansplit(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res
# --- Test Case from Example ---
if __name__ == "__main__":
    N = 5
    A = [7,2,5,10,8]
    K=3
    
    print(minimize_max_segment_sum(N, K,A))
    # Output: 14


    