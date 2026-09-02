def maxScoreFuelJourney(N, F, MAX, s):
    end=min(N,F)
    def solve(idx):
        if idx>=end+1:
            return 0
        take=s[idx]+solve(idx+1)
        not_take=solve(idx+1)
        return max(take,not_take)
    return s[0]+solve(1)
test_cases = [
    {
        "name": "Standard Positive Jump",
        "N": 5, "F": 3, "MAX": 2,
        "scores": [10, -5, 20, 15, -10],
        "expected": 45
    },
    {
        "name": "Fuel Constrained Early Stop (1 -> 2 -> 3)",
        "N": 6, "F": 2, "MAX": 3,
        "scores": [5, 10, 15, 20, 25, 30],
        "expected": 30
    },
    {
        "name": "Negative Scores - Stop at Start",
        "N": 4, "F": 3, "MAX": 2,
        "scores": [10, -5, -20, -15],
        "expected": 10
    },
    {
        "name": "Skip Negative Station using MAX jump",
        "N": 4, "F": 3, "MAX": 2,
        "scores": [10, -50, 20, 30],
        "expected": 60
    }
]

for idx, tc in enumerate(test_cases, 1):
    res = maxScoreFuelJourney(tc["N"], tc["F"], tc["MAX"], tc["scores"])
    status = "PASSED ✅" if res == tc["expected"] else f"FAILED ❌ (Got {res}, Expected {tc['expected']})"
    print(f"Test Case {idx} [{tc['name']}]: {status}")