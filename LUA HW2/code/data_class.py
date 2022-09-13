import math
import random
from misc import csv
from misc import push
from cols_class import Cols
from row_class import Row


class Data:
    def __init__(self, src):
        def func(row):
            self.add(row) 
        self.cols = None
        self.rows = []
        if type(src) == "String":
            csv(src,func)
        else:
            for row in src:
                self.add(row)
            
    
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or Row(xs))
            u = [self.cols.x, self.cols.y]
            for todo in u:
                for col in todo:
                    col.add(row.cells[col.at])
    
    def stats(self, places, showCols, fun):
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t = {}
        for col in showCols:
            v = fun(cols)
            v = type(v) == "number" and rnd(v,places) or v
            t[col.name] = v
        
        return t
        