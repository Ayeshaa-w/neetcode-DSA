def max_xor_sum(N, K, A):
    max_bits=max((max(A),K))
    current_x=0
    total_xor_sum=0
    for bit in range(max_bits,-1,-1):
        count_ones,count_zeroes=0,0
        for num in A:
            if (num>>bit)&1:
                count_ones+=1
        count_zeroes=N-count_ones
       
        candidate_x=current_x|(1<<bit)
        if candidate_x<=K and count_zeroes>count_ones:
            current_x=candidate_x
            total_xor_sum+=count_zeroes*(1<<bit)
        else:
            total_xor_sum+=count_ones*(1<<bit)
    return total_xor_sum
if __name__ == "__main__":
    N = 3
    K = 8
    A = [1, 2, 3]
    
    result = max_xor_sum(N, K, A)
    print("Maximum XOR-Sum:", result)