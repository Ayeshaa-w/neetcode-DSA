def knapsack_tabulation(weight_array, val_array, n, maxWeight):
    #base case if w_left>=weight_arr[index] use the valu eso return val[index] no it is w_left is less then cannot use so return 0 value
    dp=[[0]*(maxWeight+1) for _ in range(n)]
    for w in range(weight_array[0],maxWeight+1):
        dp[0][w]=val_array[0]
    for i in range(1,n):
        for w in range(maxWeight+1):
            no_take=0+dp[i-1][w]
            take=float('-inf')
            if w>=weight_array[i]:
                take=val_array[i]+dp[i-1][w-weight_array[i]]
            dp[i][w]=max(no_take,take)
    return dp[n-1][maxWeight]
def main():
    test_cases = [
        {
            "name": "Test Case 1 (Standard)",
            "weight_array": [4, 5, 1],
            "val_array": [1, 2, 3],
            "maxWeight": 4,
            "expected": 3,
        },
        {
            "name": "Test Case 2 (Multiple combinations)",
            "weight_array": [2, 3, 4, 5],
            "val_array": [3, 4, 5, 6],
            "maxWeight": 5,
            "expected": 7,
        },
        {
            "name": "Test Case 3 (All fit)",
            "weight_array": [1, 2, 3],
            "val_array": [10, 20, 30],
            "maxWeight": 10,
            "expected": 60,
        },
        {
            "name": "Test Case 4 (Greedy Trap)",
            "weight_array": [6, 2, 3],
            "val_array": [10, 8, 9],
            "maxWeight": 5,
            "expected": 17,
        },
    ]

    print("=" * 60)
    print(f"{'TEST CASE NAME':<35} | {'GOT':<5} | {'EXPECTED':<8} | STATUS")
    print("=" * 60)

    for tc in test_cases:
        weight_array = tc["weight_array"]
        val_array = tc["val_array"]
        n = len(weight_array)
        maxWeight = tc["maxWeight"]
        expected = tc["expected"]

        result = knapsack_tabulation(weight_array, val_array, n, maxWeight)
        status = "PASSED ✅" if result == expected else "FAILED ❌"

        print(f"{tc['name']:<35} | {result:<5} | {expected:<8} | {status}")

    print("=" * 60)


if __name__ == "__main__":
    main()