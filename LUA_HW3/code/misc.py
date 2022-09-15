from help import help
import re
import sys

settings = {
    "nums": 512,
    "seed": 10019,
    "dump": False,
    "file": "../data/auto93.csv",
    "eg": None,
    "sep": ",",
}
the = {}
class Misc:
    def __init__(self):
        def append_the(tuple):
            k=tuple.group(2)
            x=tuple.group(3)
            the[k]=self.coerce(x)
        pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
        re.sub(pattern, append_the , help)
        self.cli(the)

    def coerce(self, s):
        def fun(s1):
            if s1=="true":
                return True
            elif s1=="false":
                return False
            return s1
        if s.isnumeric():
            return int(s)
        else:
            return fun(s)

    def cli(self, t):
        for slot in t:
            v = str(t[slot])
            n = 0
            for x in sys.argv:
                if n > 0:
                    if x == "-" + slot[0] or x == "--" + slot:
                        if v == "False":
                            v = "true"
                            t[slot] = self.coerce(v)
                            continue
                        elif v == "True":
                            v = "false"
                            t[slot] = self.coerce(v)
                            continue
                        else:
                            v = sys.argv[n + 1]
                        t[slot] = self.coerce(v)
                n+=1
        if t["help"]:
            exit(help)
        return t

    def push(self,t,x):
        # t[len(t)+1] = x if t is dictionary
        t.append(x) # if t is list
        return x   

    def o(self, t):
        if type(t)!=dict:
            return str(t)
        def show(k,v):
            if "^_" not in str(k):
                v=self.o(v)
                if len(t)==0:
                    return str(k)+" "+str(v)
                else:
                    return str(v)
        u=[]
        for k in t:
            u.append(show(k,t[k]))
        if len(t)==0:
            u.sort()
        return " ".join(u)

    def oo(self, t):
        print(self.o(t))
        return t

    def rnd(self, x, places):
        mult = pow(10, places or 2)
        return math.floor(x * mult + 0.5) / mult
    
    def csv(fname, sep=None, src=None, s=None, t=None):
    print(config.settings)
    sep = config.settings["sep"]
    with open(fname) as src:
        while s := src.readline().rstrip():
            t = {}
            for y in s.split(sep):
                print(y)
                try:
                    t[1 + len(t)] = coerce(y)
                except:
                    pass

misc = Misc()
