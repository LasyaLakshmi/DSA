class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed = self.queue.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.queue[0]}")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Array Queue:", self.queue if self.queue else "Empty")

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Circular Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty! Cannot dequeue.")
            return None
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {removed}")
        return removed

    def front_elem(self):
        if self.is_empty():
            print("Circular Queue is empty!")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Circular Queue: Empty")
            return
        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

def main():
    print("=== Array-based Queue ===")
    aq = ArrayQueue()
    n = int(input("Enter total elements to enqueue: "))
    for i in range(n):
        val = int(input(f"Enter value {i+1} to enqueue: "))
        aq.enqueue(val)
    aq.display()

    d = int(input("How many elements to dequeue? "))
    for i in range(d):
        aq.dequeue()
    aq.display()
    aq.front()

    print("\n=== Circular Queue ===")
    size = int(input("Enter size of circular queue: "))
    cq = CircularQueue(size)
    n2 = int(input("Enter total elements to enqueue: "))
    for i in range(n2):
        val = int(input(f"Enter value {i+1} to enqueue: "))
        cq.enqueue(val)
    cq.display()

    d2 = int(input("How many elements to dequeue? "))
    for i in range(d2):
        cq.dequeue()
    cq.display()

    wrap_val = int(input("Enter one value to enqueue for wrap-around test: "))
    cq.enqueue(wrap_val)
    cq.display()
    cq.front_elem()

if __name__ == "__main__":
    main()
print("Tejaswini-24303")
