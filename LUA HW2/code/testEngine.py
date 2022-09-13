import random
from num_class import Num
from sym_class import Sym
from misc import the
from misc import misc

eg={}


def runs(k):
    if not eg[k]:
        return
    old = {}
    for t in the:
        old[t]=the[t]
    try:
        eg[k]
    except:
        print('error')
    for t in old:
        the[t]=old[t]
    print("!!!!!!", k)

def BAD():
    print("eg dont have this field")
    return

def LIST():
    t=[] 
    for k in eg:
        t.append(k)
    t.sort() 
    return t

def LS():
    print("\nExamples lua csv −e ...")
    for k in LIST():
        print("\t"+k)
    return True

def the_func():
    print("Values in the : ",end="")
    misc.oo(the)
    return True

def sym():
    sym = Sym()
    symbols = ["a","a","a","a","b","b","c"]
    for x in symbols:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy//1/1000
    misc.oo({"mid":mode,"div":entropy})
    return (mode =="a" and 1.37) <= (entropy and entropy <= 1.38) 

def num():
    num = Num()
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52 and 30.5<div and div<32)

def bignum():
    # Created a Num class object
    num = Num()
    the["nums"] = 32
    for i in range(1,1001):
        num.add(i)
    misc.oo(num.nums())
    return 32==num._has


def csv():
    with open("auto93.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
          print ('line[{}] = {}'.format(i, line))


def ALL():
    fails=0
    for k in LIST():
        if k != "ALL":
            print("\n---------------------")
            if not runs(k):
                fails = fails+ 1
    return True

eg["BAD"]= BAD(),
eg["LIST"]= LIST(),
eg["LS"]= LS(),
eg["ALL"]= ALL(),
eg["the"]= the_func(),
eg["sym"]= sym(),
eg["num"]= num(),
eg["bignum"]= bignum()
