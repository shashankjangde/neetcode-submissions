class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}

        # Dummy nodes
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert right before self.right
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        node = self.hmap[key]

        # Mark as recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            # Remove old node
            self.remove(self.hmap[key])

        node = Node(key, value)
        self.hmap[key] = node
        self.insert(node)

        if len(self.hmap) > self.capacity:
            # Remove least recently used
            lru = self.left.next

            self.remove(lru)
            del self.hmap[lru.key]