from misc import *
from cols_class import Cols
from row_class import Row


class Data:
    def __init__(self, src): 
        self.cols = None
        self.rows = []
        if type(src) == "str":
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
            
    
    def add(self, xs, row=None):
        if not self.cols:
            self.cols = Cols(xs)
            print("COLS", self.cols)
        else:
            self.rows[1 + len(self.rows)] = xs if "cells" in xs.keys() else Row(xs)
            for _, t in [self.cols.x, self.cols.y]:
                for col in [t]:
                    col.add(self, row.cells[col.at])
    
    def stats(self, places, showCols, fun):
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t = {}
        for col in showCols:
            v = fun(cols)
            v = type(v) == "number" and rnd(v,places) or v
            t[col.name] = v
        
        return t
        
