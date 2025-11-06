import heapq
class MinHeap:
    def _init_(self):
        self.heap=[]

    def insert(self,value):
            heapq.heappush(self.heap,value)

    def extract_min(self):
                if not self.heap:
                    return None
                return heapq.heappop(self.heap)
            
    def heapify(self,arr):
                self.heap=arr
                heapq.heapify(self.heap)

    def display(self):
                print("Min-Heap: ",self.heap)            


h=MinHeap()
arr=[3,8,67,56,2,3,5,9,11]
print("Original array: ",arr)
h.heapify(arr)
h.display()
h.insert(1)
h.display()
print("Extracted thing is: ",h.extract_min())
h.display()

import heapq
def heap_sort(arr):
    heap=arr[:]
    heapq.heapify(heap)
    sorted_list=[]
    while heap:
        smallest = heapq.heappop(heap)
        sorted_list.append(smallest)
    return sorted_list

arr=[4,30,3,25,16,9]
print("Original array: ",arr)
print("Heap sorted array: ",heap_sort(arr))