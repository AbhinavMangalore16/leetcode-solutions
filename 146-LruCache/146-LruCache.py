# Last updated: 3/31/2026, 9:39:28 PM
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.fwd = None
        self.bwd = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.beg = Node(0,0)
        self.end = Node(0,0)
        self.beg.fwd = self.end
        self.end.bwd = self.beg
    def _insert(self, node):
        nextnode = self.beg.fwd
        self.beg.fwd = node
        node.bwd = self.beg
        node.fwd = nextnode
        nextnode.bwd = node
    def _remove(self, node):
        back, front = node.bwd, node.fwd
        back.fwd = front
        front.bwd = back
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.v
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache)>self.capacity:
            lru = self.end.bwd
            self._remove(lru)
            del self.cache[lru.k]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)