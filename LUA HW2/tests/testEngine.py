import random

class Eg:

    failure = 0
    
    def BAD(self):
        print(eg.dont.have.this.field)

    def LIST(self):
        t={}; 
        for k in eg:
            t[1 + len(t)]
        t.sort() 
        return t
    
    def LS(self):
        print("\nExamples lua csv −e ...")
        for k in eg.LIST():
            print(string.format("\t%s",k))
        return True
    
    def ALL(self):
        for k in eg.LIST():
            if k != "ALL":
                print("\n---------------------")
                if not runs(k):
                    fails = fails+ 1
        return True


def runs(k):
    if not eg[k]:
        return end
    random.seed(the.seed)
    old = {}
    for k,v in the:
        old[k]=v
    if the.dump:
        status = True
        out = eg[k]
    else:
        try:
            eg[k]
        except:
            print('error')
    for k,v in old:
        the[k]=v
    msg = status and ((out==true and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k, status)
    return out or err 

