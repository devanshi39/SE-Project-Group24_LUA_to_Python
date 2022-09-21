import random
import csv
import sys
sys.path.append(sys.path[0]+'\\..\\code\\')
from num_class import Num
from sym_class import Sym
from misc import *
from utils import *

eg={}


def runs(k):
    """
    Resets random number seed before running something ,Cache the detaults settings and restore them after the test
    Print error messages or stack dumps as required or Return true if this all went well. 

    Parameters
    ----------
    k : dict
        the['eg']
    p   : int
        position from which to get the number in the list    
    
    Returns
    -------
    Bool
    """
    if k not in eg:
        return
    old = {}
    for t in the:
        old[t]=the[t]
    try:
        status = eg[k][0]()
        if status == True:
            message = "PASS"
        elif status == None:
            message = "CRASH"
        else:
            status = True
            message = "FAIL"
    except:
        status = False
        message = "CRASH"
    for t in old:
        the[t]=old[t]
    print("\n!!!!!", message, k, status)
    print(("-"*50)+"\n")
    return status

def BAD():
    """
    To test if the test still happens if something crashes
    
    Returns
    -------
    None
    """
    print("eg doesn't have this field")
    return

def LIST():
    """
    Sort all test names
        
    Returns
    -------
    list
    """
    t=[] 
    for k in eg:
        t.append(k)
    t.sort() 
    return t

def LS():
    """
    List all test names
    
    Returns
    -------
    Bool
    """
    print("\nExamples lua csv −e ...")
    for k in LIST():
        print("\t"+k)
    return True

def the_func():
    """
    Test for the
    
    Returns
    -------
    Bool
    """
    oo(the)
    return True

def sym():
    """
    Test for symbols
    
    Returns
    -------
    Bool
    """
    sym = Sym()
    symbols = ["a","a","a","a","b","b","c"]
    for x in symbols:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy//1/1000
    oo({"mid":mode,"div":entropy})
    return (mode =="a" and 1.37 <= entropy and entropy <= 1.38) 

def num():
    """
    Test for numbers
    
    Returns
    -------
    Bool
    """
    num = Num()
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52 and 30.5<div and div<32)

def bignum():
    """
    Nums store only a sample of the numbers added to it (and that storage is done such that the kept numbers span the range of inputs).
    
    Returns
    -------
    Bool
    """
    # Created a Num class object
    num = Num()
    the["nums"] = 32
    for i in range(1,1001):
        num.add(i)
    oo(num.nums())
    return len(num._has) == 32


def CSV():
    """
    To show that we can read a csv file
    
    Returns
    -------
    Bool
    """
    with open("auto93.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
          print ('line[{}] = {}'.format(i, line))
        
def data():
    """
    Load a csv file into data object
    
    Returns
    -------
    None
    """ 
  
    
    d = Data(auto93.csv)
    with open('auto93.csv') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    print(header)
    print(sorted(data, key=lambda x: (x[1], x[2], x[3])))

def stats():
    """
    Print stats on columns
    
    Returns
    -------
    None
    """ 
    with open('auto93.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',') 
        print("xmid", o( d.stats(2,d.cols.x, mid)))
        print("xdiv", o( d.stats(3,d.cols.x, div)))
        print("ymid", o( d.stats(2,d.cols.y, mid)))
        print("ydiv", o( d.stats(3,d.cols.y, div)))
    
    
def ALL():
    """
    Runs all the tests
        
    Returns
    -------
    Bool
    """
    fails=0
    l = LIST()
    for task in l:
        if task != "ALL":
            if not runs(task):
                fails = fails + 1
    return True

eg["BAD"]= BAD,
eg["LIST"]= LIST,
eg["LS"]= LS,
eg["ALL"]= ALL,
eg["the"]= the_func,
eg["sym"]= sym,
eg["num"]= num,
eg["bignum"]= bignum,
eg["csv"]= CSV,
eg["data"]= data
eg["stats"]= stats
