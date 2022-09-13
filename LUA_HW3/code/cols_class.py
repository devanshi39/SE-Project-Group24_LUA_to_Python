import math
import re
from num_class import Num
from sym_class import Sym
from misc import *

class Cols:
    def __init__(self, names = {}):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        col = None
        for c, s in names.items():
            if re.search("^[A-Z]*", s):
                col = Misc.push(self.all, Num(c,s))
            else
                col = push(self.all, Sym(c,s))
            if !re.search(":$", s):
                if re.search("[!+-]$", s):
                    Misc.push(self.y, col)
                else:
                    push(self.x, col)
            else re.search("!$", s):
                self.klass = col