import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def heapify(self, iterable):
        self.heap = list(iterable)
        heapq.heapify(self.heap)

    def __str__(self):
        return str(self.heap)

def heapsort(iterable):
    h = MinHeap()
    h.heapify(iterable)
    sorted_list = []
    while h.heap:
        sorted_list.append(h.extract_min())
    return sorted_list

# Take input from user as space-separated integers
user_input = input("Enter numbers separated by space: ")
test_list = list(map(int, user_input.split()))

# Test MinHeap operations
min_heap = MinHeap()
min_heap.heapify(test_list)
print("Heap after heapify:", min_heap)

min_heap.insert(5)
print("Heap after inserting 5:", min_heap)

min_val = min_heap.extract_min()
print("Extracted min:", min_val)
print("Heap after extracting min:", min_heap)

# Test heapsort
sorted_list = heapsort(test_list)
print("Heapsort result:", sorted_list)
print("Tejaswini-24303")
