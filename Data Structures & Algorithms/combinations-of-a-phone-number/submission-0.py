class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        mapping= {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def bactrack(i,curr):
            if i>=len(digits):
                res.append(curr)
                return
            for c in mapping[digits[i]]:
                bactrack(i+1,curr+c)
        if digits:
            bactrack(0,"")
        return res
        