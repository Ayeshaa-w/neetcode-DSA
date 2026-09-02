def minimize_ugliness(S: str, CASH: int, A: int, B: int) -> int:
    s=list(S)
    n=len(s)
    zero_indices=[i for i in range(n) if s[i]=='0']
    zero_pointer=0
    for i in range(n):
        if CASH<=0:
            break
        if s[i]=='1':
            while zero_pointer<len(zero_indices) and zero_indices[zero_pointer]<=i:
                zero_pointer+=1
            has_pointer=zero_pointer<len(zero_indices)
            if has_pointer and  A<=B and CASH>=A:
                s[i],s[zero_indices[zero_pointer]]='0','1'
                zero_pointer+=1
                CASH-=A
            elif CASH>=B:
                s[i]='0'
                CASH-=B
    return int("".join(s),2)
if __name__ == "__main__":
    result = minimize_ugliness("1101101", CASH=6, A=2, B=3)
    print("Final Output (Decimal Ugliness):", result)  # Outputs: 31