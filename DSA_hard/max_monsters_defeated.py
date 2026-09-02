def max_monsters_defeated(N: int, e: int, power: list[int], bonus: list[int]) -> int:
    hashdict=[]
    for i in range(N):
        hashdict.append([power[i],bonus[i]])
    hashdict=sorted(hashdict,key=lambda x:x[0])
    defeat=0
    for power,bonus in hashdict:
        if e<power:
            return defeat
        else:
            e+=bonus
            defeat+=1
    return defeat
print(max_monsters_defeated(4,1,[5, 2, 8, 1],[3, 1, 4, 1]))
#THE GREEDY APPROCH INVOLVES THINKING HOW TO LIMIT THE ITERATIONS DAY BY SORTING THEN IF MINIMUM DOESNT GET SATISFIES THE MAXIMUM CAN NEVER BE SOLVED THIS IS THE GREEDY THINKING PROCESS


