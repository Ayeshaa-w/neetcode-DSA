def max_xor_sum(N, K, A):
    max_bits=max((max(A),K))
    current_x=0 #current bit msb of x is set to 0
    total_xor_sum=0 #adds all the A values in the nth bit with x bit.
    for bit in range(max_bits,-1,-1):
        count_ones,count_zeroes=0,0
        for num in A:
            if (num>>bit)&1:#>> right shift bit times it will come to the right side automatically &1 gives boolean is it 1 or not?
                count_ones+=1
        count_zeroes=N-count_ones
       
        candidate_x=current_x|(1<<bit) #30*10 numerics,1*2^3+0*2^4 etc we r or the value
        if candidate_x<=K and count_zeroes>count_ones:#if x bit is set as 1 and countzeroes in array is greter we get result 1
            current_x=candidate_x#updating x bit as 1
            total_xor_sum+=count_zeroes*(1<<bit) #0 adds up to the sum value
        else:
            total_xor_sum+=count_ones*(1<<bit) #aarray values having ones contribute to the sum
    return total_xor_sum
if __name__ == "__main__":
    N = 3
    K = 8
    A = [1, 2, 3]
    
    result = max_xor_sum(N, K, A)
    print("Maximum XOR-Sum:", result)