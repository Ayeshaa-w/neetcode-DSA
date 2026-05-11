class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = {}
        window = {}
        have = 0
        string = ""
        res = float('inf')

        for i in t:
            countt[i] = countt.get(i, 0) + 1

        need = len(countt)

        l = 0

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countt and window[s[r]] == countt[s[r]]:
                have += 1

            while have == need:

                dist = r - l + 1
                if dist < res:
                    res = dist
                    string = s[l:r+1]

                window[s[l]] -= 1

                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have -= 1

                l += 1

        return string






        