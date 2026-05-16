class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next, self.r.prev = self.r, self.l

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev = self.r.prev
        prev.next, self.r.prev = node, node
        node.prev, node.next = prev, self.r

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.l.next
            self.remove(lru)
            del self.cache[lru.key]