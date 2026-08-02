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

