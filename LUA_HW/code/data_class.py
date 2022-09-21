from misc import *
from cols_class import Cols
from row_class import Row


class Data:
    """
    Data class holds all the required data in the csv file in the form of rows and columns.

    ...

    Attributes
    ----------
    cols : dict
         stores the summary of data in column
    rows : list
        stores the list of all the rows
    
    
    """
    def __init__(self, src): 
        self.cols = None
        self.rows = []
        if type(src) == "str":
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
            
    
    def add(self, xs, row=None):
        """
        This method adds the data to the rows as we encounter them in the csv file.Calls add() to updatie the cols with new values.

        Parameters
        ----------
        xs : dict
             this is the row that we want to add in the rows list in the data object.

        Returns
        -------
        None
        """
        if not self.cols:
            self.cols = Cols(xs)
            print("COLS", self.cols)
        else:
            self.rows[1 + len(self.rows)] = xs if "cells" in xs.keys() else Row(xs)
            for _, t in [self.cols.x, self.cols.y]:
                for col in [t]:
                    col.add(self, row.cells[col.at])
    
    def stats(self, places, showCols, fun):
        """
        This method derives the stats like median and deviation for various columns
        For showCols (default=data.cols.x) in data ,show fun (default=mid),
        rounding numbers to places (default=2)
        Parameters
        ----------
        showCols : list
            list of either dependent or independent columns
        places : int
            list of either dependent or independent columns
        fun : str 
            function to be called for calculating median or deviation for columns
        Returns
        -------
        dict
        """
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t = {}
        for col in showCols:
            v = fun(cols)
            v = type(v) == "number" and rnd(v,places) or v
            t[col.name] = v
        
        return t
        
