from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.q = deque([])
        self.cache = {} 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key) 
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:    
            self.q.remove(key)
            self.q.append(key)
            self.cache[key] = value
            return

        if len(self.q) < self.capacity:
            self.q.append(key)
            self.cache[key] = value
        else:
            removed = self.q.popleft()
            del self.cache[removed]
            self.q.append(key)
            self.cache[key] = value
            
            
# Hashmap to store key value pair. Queue or Doubly Linked List to record the sequence of the keys used.
# Get: Get value in the hasmap if it exists. Update the the recency of the key in the queue/DLL. If it doesn't exist return -1.
# Put: If it's in the q/DLL update recency and return update the value.
# If not in cache replace the key value and add to the q/dll
# If in cache remove least recent element delete from cache. Add key value to cache and key to recency q/DLL.