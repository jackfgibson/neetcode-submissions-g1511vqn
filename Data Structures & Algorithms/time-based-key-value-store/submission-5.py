class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key):
            return ""
        l, r = 0, len(self.store.get(key))-1
        recent = ""
        while l<=r:
            m = (l+r)//2
            if self.store.get(key)[m][1] <= timestamp:
                recent = self.store.get(key)[m][0]
                l = m+1
            else:
                r = m-1
        return recent