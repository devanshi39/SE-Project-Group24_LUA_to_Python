import math
import re
from num_class import Num
from sym_class import Sym
from misc import *

class Cols:
    """
    Cols class holds the summaries of columns.It decides which column is skipped, independent or depenedent and stores it accordingly into
    all - stores all the columns, x - only independent columns, y - only dependent columns. Columns are created just once and then may appear in 
    multiple slots.

    ...

    Attributes
    ----------
    name : dict
        stores all the column names
    all : int
        stores all the columns including the skipped ones
    klass : str
        if a single dependent class column exist we store it here.
    x : list
        stores all the independent columns that are not skipped
    y : list
        stores all the dependent columns that are not skipped

    
    """
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
            else:
                col = push(self.all, Sym(c,s))
            if not re.search(":$", s):
                if re.search("[!+-]$", s):
                    Misc.push(self.y, col)
                else:
                    push(self.x, col)
                if re.search("!$", s):
                    self.klass = col
