from collections import Counter, deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        q = deque()
        in_queue = set()
        result = []
        total = 0

        for ch in s:
            count[ch] -= 1
            total += 1

            if ch not in in_queue:
                q.append(ch)
                in_queue.add(ch)

            # drain front of queue for all chars fully seen
            while q and count[q[0]] == 0:
                removed = q.popleft()
                in_queue.discard(removed)

            if not q:
                result.append(total)
                total = 0

        return result