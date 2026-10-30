class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()
        seen.add(source)

        def f(i):
            if i==destination:
                return True
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    if f(nei):
                        return True
            return False
        return f(source)