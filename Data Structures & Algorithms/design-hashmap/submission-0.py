class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        # A fixed-size array of buckets using a prime number to reduce collisions
        self.size = 1000
        # Initialize each bucket with a dummy head node to simplify insertions/deletions
        self.map = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        curr = self.map[index]

        # Traverse the chain to check if key already exists
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value  # Update existing key's value
                return
            curr = curr.next

        # If key is not found, append a new node at the end
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.map[index].next  # Skip dummy node

        # Search for key in the bucket
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1  # Key not found

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.map[index]

        # Search for the predecessor node of the key to be deleted
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Unlink the target node
                return
            curr = curr.next