def min_swaps_brute_force_char(s,ch):
    indices=[i for i in range(len(s)) if s[i]==ch]
    k=len(indices)
    if k<=0:
        return 0
    min_swaps=float('inf')
    for S in range(len(s)-k+1):
        current_swaps=0
        for j in range(k):
            target=S+j
            current_swaps+=abs(indices[j]-target)
        min_swaps=min(min_swaps,current_swaps)
    return min_swaps
def min_swaps_brute_force(s: str) -> int:
    
    swaps_for_ones = min_swaps_brute_force_char(s, '1')
    swaps_for_zeros = min_swaps_brute_force_char(s, '0')
    
    return min(swaps_for_ones, swaps_for_zeros)


# Example test run
if __name__ == "__main__":
    test_str = "10101"
    print("Min swaps for '1001':", min_swaps_brute_force(test_str))  # Output: 0



#optimal solution
def min_swaps_for_char(s,ch):
    indices=[i for i in range(len(s)) if s[i]==ch]
    adjusted=[indices[i]-i for i in range(len(indices))]
    median=len(adjusted)//2
    return sum(abs(c-median) for i,c in enumerate(adjusted))
def min_adjacent_swaps(s):
    cost_ones = min_swaps_for_char(s, '1')
    cost_zeros = min_swaps_for_char(s, '0')
    return min(cost_ones, cost_zeros)
if __name__ == "__main__":
    test_str = "1001"
    print("Min swaps for '1001':", min_adjacent_swaps(test_str)) 