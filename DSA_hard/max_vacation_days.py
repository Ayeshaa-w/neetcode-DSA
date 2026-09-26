def max_vacation_days(total_days,k,obligations):
    obs=[0]+obligations+[total_days+1]
    max_vac=0
    if k>=len(obligations):
        return total_days
    for i in range(1,len(obligations)-k):
        left_bound=obs[i-1]
        right_bound=obs[i+k]
        vacation=(right_bound-1)-(left_bound+1)+1
        max_vac=max(max_vac,vacation)
    return max_vac
total_days = 20
K = 2
obligations = [3, 8, 12, 15, 18]

print(max_vacation_days(total_days, K, obligations))
