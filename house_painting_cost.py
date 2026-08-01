def house_painting(paints):
    if not paints:
        return 0
    memo={}
    def solve(idx,clr):
        if idx>=len(paints):
            return 0
        if (idx,clr) in memo:
            return memo[((idx,clr))]
        min_val=float('inf')
        for c in range(3):
            if c!=clr:
                res=paints[idx][c]+solve(idx+1,c)
                min_val=min(min_val,res)
        memo[(idx,clr)]=min_val
        return min_val
    return solve(0,-1)
if __name__ == "__main__":
    test_str = [[1, 5, 3], [2, 9, 3], [3, 1, 7]]
    b = 20
    ans = house_painting(test_str)
    print(ans if ans <= b else -1)
def min_paint_cost(costs, budget):
    if not costs:
        return 0
    dp_red,dp_blue,dp_green=costs[0][0],costs[1][0],costs[2][0]
    for i in range(1,len(costs)):
        new_red=costs[i][0]+min(dp_blue,dp_green)
        new_blue=costs[i][1]+min(dp_green,dp_red)
        new_green=costs[i][2]+min(dp_red,dp_blue)
        dp_red,dp_blue,dp_green=new_red,new_blue,new_green
        
    min_cost=min(new_red,new_blue,new_green)
    return min_cost if min_cost<=b else -1
if __name__ == "__main__":
    test_str = [[1, 5, 3], [2, 9, 3], [3, 1, 7]]
    b = 20
    print(min_paint_cost(test_str,b))
