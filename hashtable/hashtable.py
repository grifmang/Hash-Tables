class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.entries = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

        fnv_prime = 1099511628211
        fnv_offset_basis = 14695981039346656037

        hash = fnv_offset_basis

        str_bytes = str(key).encode()

        for letter in str_bytes:
            hash *= fnv_prime
            hash ^= letter
        
        hash &= 0xffffffffffffffff

        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381

        str_bytes = str(key).encode()

        for letter in str_bytes:
            hash *= 33 + letter

        hash &= 0xffffffff

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def load_factor(self):
        return self.entries / self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # new_node = HashTableEntry(key, value)
        hi = self.hash_index(key)
        # node = self.storage[hi]

        if self.storage[hi] is None:
            # If the index to place the new node is empty, fill it with a HashTableEntry
            self.storage[hi] = HashTableEntry(key, value)
            self.entries += 1

            # if self.load_factor() > 0.7:
            #     self.resize(self.capacity * 2)
        else:
            # Make new node
            new_node = HashTableEntry(key, value)
            # Make head the next pointer
            new_node.next = self.storage[hi]
            # Make new head
            self.storage[hi] = new_node
            self.entries += 1
            
            # if self.load_factor() > 0.7:
            #     self.resize(self.capacity * 2)
            # while node.next is not None and node.key != key:
            #     node = node.next
            
            # if node.key == key:
            #     node = HashTableEntry(key, value)
            #     self.entries += 1
            # else:
            #     node.next = HashTableEntry(key, value)
            #     self.entries += 1
            
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hi = self.hash_index(key)
        node = self.storage[hi]
        prev = None

        while node.next is not None and node.next.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            if prev is None:
                self.storage[hi] = node.next
            else:
                prev.next = prev.next.next
                self.entries -= 1
                # if self.load_factor() < 0.2:
                #     self.resize(self.capacity // 2)
                return None
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hi = self.hash_index(key)
        node = self.storage[hi]

        if node == None:
            return None

        while node.next is not None and node.key != key:
            node = node.next

        return node.value
        
    def resize(self, size):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        new_array = [None] * size
        self.entries = 0

        for element in self.storage:
            while element:
                new_index = self.hash_index(element.key)
                if not new_array[new_index]:
                    new_array[new_index] = HashTableEntry(element.key, element.value)
                    self.entries += 1
                else:
                    new_node = HashTableEntry(element.key, element.value)
                    new_node.next = new_array[new_index]
                    new_array[new_index] = new_node
                    self.entries += 1
                element = element.next

        # print('storage', self.storage)
        # print('new_storage', new_array)
        # print('entries', self.entries)
        # print('length', len(new_array))
        self.storage = new_array
        return self.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
