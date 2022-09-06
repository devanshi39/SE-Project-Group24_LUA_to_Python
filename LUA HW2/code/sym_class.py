import math

class Sym:
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []

    def add(self, v):
        if v!="?":
            self.n=self.n+1
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self):
        most=-1
        for k in self._has:
            v=self._has[k]
            if v>most:
                mode, most=k,v
        return mode

    def div(self):
        def fun(p):
            return p*(math.log(p,2))
        e=0
        for k in self._has:
            n=self._has[k]
            if n>0:
                e=e-fun(n/self.n)
        return e