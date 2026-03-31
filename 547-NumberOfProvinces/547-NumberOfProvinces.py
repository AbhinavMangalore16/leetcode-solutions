# Last updated: 3/31/2026, 9:37:36 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes = len(isConnected)
        def DFS(node, visited):
            visited[node] = True
            for neighbour in range(len(isConnected)):
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                    DFS(neighbour, visited)
        visited = [False]*(nodes+1)
        c = 0
        for node in range(nodes):
            if not visited[node]:
                DFS(node, visited)
                c+=1
        return c