import math
from misc import the,coerce

def o(t):
    if type(t)!=dict:
        return str(t)
    def show(k,v):
        if "^_" not in str(k):
            v=o(v)
            return str(k)+" : "+str(v)
    u=[]
    for k in t:
        u.append(show(k,t[k]))
    if len(t)==0:
        u.sort()
    return " ".join(u)

def oo(t):
    print(o(t))
    return t

def rnd(x, places):
    mult = pow(10, places or 2)
    return math.floor(x * mult + 0.5) / mult

def csv(fname, sep=None, src=None, s=None, t=None):
    sep = the["sep"]
    with open(fname) as src:
        while s := src.readline().rstrip():
            t = {}
            for y in s.split(sep):
                print(y)
                try:
                    t[1 + len(t)] = coerce(y)
                except:
                    pass