def process_heat_query(heat, L, R, d, k, c):
    candidates=[]
    for i in range(L,R+1):
        if heat[i]>=c:
            val=heat[i]*4
        else:
            val=heat[i]
        candidates.append([val,i])
    candidates.sort(key=lambda x:x[0] ,reverse=True)
    res=[]
    total=0
    for value,idx in candidates:
        if len(res)==k:
            break
        valid=True
        for prev in res:
            if abs(prev-idx)<d:
                valid=False
                break
        if valid:
            res.append(idx)
            total+=value
    return total if len(res)==k else -1
heat = [5, 5, 5]
# Range L=0, R=2 | dist d=1 | pick k=2 | critical threshold c=0
print(process_heat_query(heat, L=0, R=2, d=1, k=3, c=0))
