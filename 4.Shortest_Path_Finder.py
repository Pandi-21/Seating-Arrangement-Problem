# Problem:
# Find the shortest path between two cities in a weighted graph using Dijkstra's Algorithm.

# solution:
# - Use a priority queue (min-heap) to always expand the city with the smallest distance.
# - Track the shortest distance and the path taken to reach each city.
# - Stop when the destination city is reached.

import heapq

def shortest_Path(cities, start, desti):#desti= destination
    heap = [(0, start, [start])]  # (total_distance, current_city, path_taken)
    visited = set()
    
    while heap:
        distance, current_city, path = heapq.heappop(heap)
        
        if current_city == desti:
            print(f"Shortest path from {start} to {desti}: {' -> '.join(path)}")
            print(f"Total distance: {distance}")
            return
        
        if current_city in visited:
            continue
        
        visited.add(current_city)
        
        for travel, weight in cities[current_city].items():
            if travel not in visited:
                heapq.heappush(heap, (distance + weight, travel, path + [travel]))
    
    print(f"Not founded from {start} to {desti}")

 
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

shortest_Path(cities, start_city, destination_city)
