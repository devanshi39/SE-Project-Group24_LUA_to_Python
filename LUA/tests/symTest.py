class Eg:
    pass
  
eg = Eg()
  
def sym(sym,entropy,mode):
    sym = Sym();
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



