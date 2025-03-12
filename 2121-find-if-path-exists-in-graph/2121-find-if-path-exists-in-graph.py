# from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dict=defaultdict(list)
        for i in range(len(edges)):
            u=edges[i][0]
            v=edges[i][1]
            dict[u].append(v)
            dict[v].append(u)
        queue=deque([(source)])
        visit={source}
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for ngh in dict[node]:
                if ngh not in visit:
                    visit.add(ngh)
                    queue.append(ngh)
        return False
