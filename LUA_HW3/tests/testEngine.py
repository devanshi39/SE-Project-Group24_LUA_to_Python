import random
import csv
import sys
sys.path.append('../code')
from num_class import Num
from sym_class import Sym
from misc import *

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
    print("eg doesn't have this field")
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
    Misc.oo(the)
    return True

def sym():
    sym = Sym()
    symbols = ["a","a","a","a","b","b","c"]
    for x in symbols:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy//1/1000
    Misc.oo({"mid":mode,"div":entropy})
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
    Misc.oo(num.nums())
    return 32==num._has


def csv():
    with open("auto93.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
          print ('line[{}] = {}'.format(i, line))
        
def data():
  # Created a Data class object
  d = Data(auto93.csv)
  with open('auto93.csv') as f:
      reader = csv.reader(f)
      header = next(reader)
      data = [row for row in reader]
  print(header)
  print(sorted(data, key=lambda x: (x[1], x[2], x[3])))

def stats():
    # Created a Data class object
    with open('auto93.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',') 
    print("xmid", Misc.o( d.stats(2,d.cols.x, mid)))
    print("xdiv", Misc.o( d.stats(3,d.cols.x, div)))
    print("ymid", Misc.o( d.stats(2,d.cols.y, mid)))
    print("ydiv", Misc.o( d.stats(3,d.cols.y, div)))
    
    
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
eg["csv"]= csv()
eg["data"]= data()