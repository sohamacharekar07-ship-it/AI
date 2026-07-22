from collections import deque
import heapq
# --------------------------------------------------
# Graph (Based on Google Maps Route)
# --------------------------------------------------
graph = {
    "Raheja College": [("BKC Junction", 2)],
    "BKC Junction": [("Vakola", 2)],
    "Vakola": [("Airport", 2)],
    "Airport": [("Saki Naka", 2), ("Marol", 2)],
    "Saki Naka": [("Home", 1.4)],
    "Marol": [("Home", 3)],
    "Home": []
}
# --------------------------------------------------
# Heuristic Values (Distance to Home)
# --------------------------------------------------
heuristic = {
    "Raheja College": 9.4,
    "BKC Junction": 7.4,
    "Vakola": 5.4,
    "Airport": 3.4,
    "Saki Naka": 1.4,
    "Marol": 2.8,
    "Home": 0
}
# --------------------------------------------------
# Breadth First Search (BFS)
# --------------------------------------------------
def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    explored = 0
    while queue:
        node, path, cost = queue.popleft()
        explored += 1
        if node == goal:
            return path, cost, explored
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in graph[node]:
                queue.append((neighbour,
                              path + [neighbour],
                              cost + edge_cost))

# --------------------------------------------------
# Depth First Search (DFS)
# --------------------------------------------------
def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    explored = 0
    while stack:
        node, path, cost = stack.pop()
        explored += 1
        if node == goal:
            return path, cost, explored
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in reversed(graph[node]):
                stack.append((neighbour,
                              path + [neighbour],
                              cost + edge_cost))
# --------------------------------------------------
# Uniform Cost Search (UCS)
# --------------------------------------------------
def ucs(start, goal):
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = set()
    explored = 0
    while queue:
        cost, node, path = heapq.heappop(queue)
        explored += 1
        if node == goal:
            return path, cost, explored
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in graph[node]:
                heapq.heappush(queue,
                               (cost + edge_cost,
                                neighbour,
                                path + [neighbour]))
# --------------------------------------------------
# Greedy Best First Search
# --------------------------------------------------
def greedy(start, goal):
    queue = []
    heapq.heappush(queue,
                   (heuristic[start],
                    start,
                    [start],
                    0))
    visited = set()
    explored = 0
    while queue:
        h, node, path, cost = heapq.heappop(queue)
        explored += 1
        if node == goal:
            return path, cost, explored
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in graph[node]:
                heapq.heappush(queue,
                               (heuristic[neighbour],
                                neighbour,
                                path + [neighbour],
                                cost + edge_cost))
# --------------------------------------------------
# A* Search
# --------------------------------------------------
def astar(start, goal):
    queue = []
    heapq.heappush(queue,
                   (heuristic[start],
                    0,
                    start,
                    [start]))
    visited = set()
    explored = 0
    while queue:
        f, g, node, path = heapq.heappop(queue)
        explored += 1
        if node == goal:
            return path, g, explored
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in graph[node]:
                new_g = g + edge_cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(queue,
                               (new_f,
                                new_g,
                                neighbour,
                                path + [neighbour]))
# --------------------------------------------------
# Display Function
# --------------------------------------------------
def display(name, result):
    path, cost, explored = result
    print("\n===================================")
    print(name)
    print("===================================")
    print("Path :", " -> ".join(path))
    print("Total Cost :", cost, "km")
    print("Nodes Explored :", explored)
# --------------------------------------------------
# Main Program
# --------------------------------------------------
start = "Raheja College"
goal = "Home"
display("Breadth First Search (BFS)", bfs(start, goal))
display("Depth First Search (DFS)", dfs(start, goal))
display("Uniform Cost Search (UCS)", ucs(start, goal))
display("Greedy Best First Search", greedy(start, goal))
display("A* Search", astar(start, goal))
