# This file has all the tests
import module

def the():
    oo(the)
  
def sym(sym,entropy,mode):
    sym = Sym()
    symbols = ["a","a","a","a","b","b","c"]
    for x in symbols:
        sym.add(x)
    mid = sym.mid()
    div = sym.div()
    entropy = 1000*entropy
    operation  = {}
    operation['mid'] = mid
    operation['div'] =  entropy
    oo(operation)
    return (mode =="a" and 1.37) <= (entropy and entropy <= 1.38) 


def num():
    num = module.Num()
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52 and 30.5<div and div<32)

def bignum():
    # Created a Num class object
    num = module.Num()
    the.nums = 32
    for i in range(1,1001):
        num.add(i)
    #oo(num:nums())
    return 32==num._has
