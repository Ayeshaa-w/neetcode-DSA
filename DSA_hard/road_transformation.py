def road_transformation(n,k,arr):
    l,r=0,max(arr)
    while l<=r:
        mid=l+((r-l)//2)
        total=0
        for i in arr:
            if i>mid:
                total+=i-mid
        if total<=k:
            res=mid
            r=mid-1
        elif total>k:
            l=mid+1
    return res
print(road_transformation(5,3,[3,5,2,8,4]))