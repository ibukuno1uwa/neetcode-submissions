class DoublyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = DoublyNode(0, 0)
        self.tail = DoublyNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DoublyNode):
        node.prev.next = node.next 
        node.next.prev = node.prev

    def _add(self, node: DoublyNode):
        self.tail.prev.next = node

        node.prev = self.tail.prev
        self.tail.prev = node

        node.next = self.tail


    def get(self, key: int) -> int:
        if key in self.cache:
            MRU = self.cache[key]
            self._remove(MRU)
            self._add(MRU)

            return MRU.val

        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            prev_node = self.cache[key]
            self._remove(prev_node)

        node = DoublyNode(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            # remove LRU
            LRU = self.head.next
            self._remove(LRU)
            self.cache.pop(LRU.key)
        
