class MinStack:

    def __init__(self):
        self.array = []
        self.small = None
        self.smallTrack = []

    def push(self, val: int) -> None:
        if self.small == None or val < self.small:
            self.small = val
            self.smallTrack.append(val)
        elif val == self.small:
            self.smallTrack.append(val)
        self.array.append(val)

    def pop(self) -> None:
        top = self.array[-1]
        if top == self.small:
            self.smallTrack = self.smallTrack[:-1]
            if len(self.smallTrack)>0:
                self.small = self.smallTrack[-1]
            else:
                self.small = None
        self.array = self.array[:-1]
        return top

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.small
