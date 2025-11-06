# Node class
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def _init_(self):
        self.head = None

    # Insert at front
    def InsertFront(self,data):
        New_Node = Node(data)
        New_Node.next = self.head
        self.head = New_Node

    # Insert at end
    def InsertEnd(self,data):
        New_Node = Node(data)
        if self.head == None:
            self.head = New_Node
            return
        else:
            ptr = self.head
            #loop till end
            while ptr.next:
                ptr = ptr.next
            ptr.next = New_Node
    
    # Delete at front
    def DeleteFront(self):
        if self.head == None:
            print("LinkedList is Empty")
            return
        else:
            self.head = self.head.next

    # Delete at back
    def DeleteEnd(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None

    #Search
    def Search(self, data):
        ptr = self.head
        pos = 0
        while ptr:
            if ptr.data == data:
                print(f"Element {data} found at position {pos}.")
                return
            ptr = ptr.next
            pos += 1
        print(f"Element {data} not found in the list.")
    
    # Traverse the LinkedList
    def Traverse(self):
        ptr = self.head
        while ptr:
            print(ptr.data,end="-->")
            ptr = ptr.next
        print("NULL")

# Testing
LL = LinkedList()
LL.InsertFront(10)
LL.InsertFront(5)
LL.InsertEnd(20)
LL.Traverse()
LL.DeleteFront()
LL.DeleteEnd()
LL.Traverse()
LL.Search(10)