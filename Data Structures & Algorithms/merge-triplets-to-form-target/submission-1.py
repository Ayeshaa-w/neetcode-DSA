class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        at, bt, ct = target
        found_a = found_b = found_c = False
        
        for a, b, c in triplets:
            # Skip any triplet that has a value greater than the target
            if a > at or b > bt or c > ct:
                continue
                
            # If it's valid, check if it matches target components
            if a == at: found_a = True
            if b == bt: found_b = True
            if c == ct: found_c = True
            
            # Optimization: Early exit if all targets are found
            if found_a and found_b and found_c:
                return True
                
        return False