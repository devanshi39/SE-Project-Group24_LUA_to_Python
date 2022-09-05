#sym methods
import math
def add(int v):
	if v!="?":
		n=n+1
		if has[v]:
			has[v]=1+has[v]

def mid(col, most, mode):
	most=-1
	for k,v in has:
		if v>most:
			mode, most=k,v
	return mode

def div(e, fun):
	def fun(p):
		return p*(math.log(p,2))
	e=0
	for n in self._has:
		if n>0:
			e=e-fun(n//self.n)
	return e
		