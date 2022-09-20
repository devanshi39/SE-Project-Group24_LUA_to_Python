from help import help
import math
import re
import sys

the = {
    "nums": 512,
    "seed": 10019,
    "dump": False,
    "file": "../data/auto93.csv",
    "eg": None,
    "sep": ","
}

def coerce(s):
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

class CLI:
    def __init__(self):
        def append_the(tuple):
            k=tuple.group(2)
            x=tuple.group(3)
            the[k]=coerce(x)
        pattern = r"-(\w+)[\s]*--[\s]*(\w+)[\s]*[^=]*[\s]*=[\s]*(.*)"
        re.sub(pattern, append_the , help)
        self.cli(the)

    def cli(self, t):
        for slot in t:
            v = str(t[slot])
            n = 0
            for x in sys.argv:
                if n > 0:
                    if x == "-" + slot[0] or x == "--" + slot:
                        if v == "False":
                            v = "true"
                            t[slot] = coerce(v)
                            continue
                        elif v == "True":
                            v = "false"
                            t[slot] = coerce(v)
                            continue
                        else:
                            v = sys.argv[n + 1]
                        t[slot] = coerce(v)
                n+=1
        if t["help"]:
            exit(help)
        return t

    def push(self,t,x):
        # t[len(t)+1] = x if t is dictionary
        t.append(x) # if t is list
        return x
   