import heapq
import hashlib

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Bloom filter implementation
class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for i in range(self.hash_count):
            hash_obj = hashlib.md5(f'{item}{i}'.encode())
            hash_value = int(hash_obj.hexdigest(), 16) % self.size
            hashes.append(hash_value)
        return hashes

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def query(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))
# Dijkstra's part
n = int(input("Enter number of nodes: "))
nodes = input("Enter node names separated by space: ").split()
m = int(input("Enter number of edges: "))

graph = {node: {} for node in nodes}
print("Enter edges in format 'U V W' (e.g. A B 4):")
for _ in range(m):
    u, v, w = input().split()
    w = int(w)
    graph[u][v] = w
    graph[v][u] = w  # undirected

start = input("Enter start node for Dijkstra: ")
print("\nDijkstra’s shortest paths:")
distances = dijkstra(graph, start)
for node in distances:
    print(f"Distance from {start} to {node}: {distances[node]}")

# Bloom filter part
bf = BloomFilter()
insert_items = input("\nEnter items to insert into Bloom filter (e.g. apple banana): ").split()
for item in insert_items:
    bf.add(item)

query_items = input("Enter items to query (e.g. apple orange): ").split()
print("\nBloom filter query results:")
for q in query_items:
    print(f"{q}: {bf.query(q)}")
print("Tejaswini-24303")
