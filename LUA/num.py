import math

class Num:
    def __init__(self, c, s):
        self.n = 0
        self.c = c
        self.at = c || 0
        self.s = s
        self.name = s || ""
        self._has = {}
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True