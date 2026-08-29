class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:

        # Create adjacency list
        graph = [[] for _ in range(n)]

        # Build the graph
        for a, b in paths:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)

        # Store flower assigned to each garden
        ans = [0] * n

        # Assign flowers
        for i in range(n):

            # Flowers used by neighboring gardens
            used = set()

            for neighbor in graph[i]:
                if ans[neighbor] != 0:
                    used.add(ans[neighbor])

            # Choose the first available flower
            for flower in range(1, 5):
                if flower not in used:
                    ans[i] = flower
                    break

        return ans