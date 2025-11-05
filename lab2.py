class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def del_first(self):
        if not self.head:
            print("List is empty! Cannot delete.")
            return
        print(f"Deleted from front: {self.head.data}")
        self.head = self.head.next

    def print_list(self):
        curr = self.head
        if not curr:
            print("List is empty.")
            return
        print("Linked List: ", end="")
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Popped: {popped_data}")
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def display(self):
        curr = self.top
        if not curr:
            print("Stack is empty.")
            return
        print("Stack (top -> bottom): ", end="")
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

def main():
    print("=== Singly Linked List Operations ===")
    ll = LinkedList()
    n = int(input("How many elements to insert at front? "))
    for i in range(n):
        val = int(input(f"Enter value {i + 1} to insert at front: "))
        ll.add_first(val)
        ll.print_list()

    m = int(input("How many elements to insert at end? "))
    for i in range(m):
        val = int(input(f"Enter value {i + 1} to insert at end: "))
        ll.add_last(val)
        ll.print_list()

    print("\nDeleting the front node...")
    ll.del_first()
    ll.print_list()
    print("Traversing linked list:")
    ll.print_list()

    print("\n=== Stack Operations Using Linked List ===")
    stack = Stack()
    p = int(input("How many elements to push onto stack? "))
    for i in range(p):
        val = int(input(f"Enter value {i + 1} to push: "))
        stack.push(val)
        stack.display()

    print("\nPerforming one pop operation from stack...")
    stack.pop()
    stack.display()

    print("\nPeeking top element of the stack...")
    stack.peek()

if __name__ == "__main__":
    main()
print("Tejaswini-24303")    
