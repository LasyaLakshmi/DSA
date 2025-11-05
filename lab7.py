class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<deleted>"

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None and self.table[idx] != self.DELETED:
            idx = (idx + 1) % self.size
            if idx == start_idx:
                print("Hash table is full, cannot insert", key)
                return
        self.table[idx] = key

    def search(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return idx
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return -1

    def delete(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx] == key:
                self.table[idx] = self.DELETED
                return True
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return False

    def display(self):
        print(self.table)

ht = HashTable()
num_keys = int(input("Enter number of keys to insert: "))
print("Enter keys one by one:")
for _ in range(num_keys):
    key = int(input())
    ht.insert(key)
print("Hash table after inserts:")
ht.display()
search_key = int(input("Enter a key to search: "))
search_index = ht.search(search_key)
print(f"Search for {search_key}:", f"Found at index {search_index}" if search_index != -1 else "Not found")
delete_key = int(input("Enter a key to delete: "))
deleted = ht.delete(delete_key)
print(f"Delete {delete_key}:", "Successful" if deleted else "Key not found")
print("Hash table after deleting", delete_key, ":")
ht.display()
print("Tejaswini-24303")

