class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,time in times:
            graph[u].append([v,time])#directed
        min_heap=[(0,k)]
        res_max_cost=0
        visited=set()
        while min_heap:
            current_cost,current_node=heapq.heappop(min_heap)
            if current_node in visited:
                continue
            visited.add(current_node)
            res_max_cost=current_cost
            for nei,cost in graph[current_node]:
                if nei not in visited:
                    heapq.heappush(min_heap,(current_cost+cost,nei))
        return res_max_cost if len(visited)==n else -1
        