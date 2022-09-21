import copy

class Row:
    """
    Row class holds one record/row of the csv file
    ...

    Attributes
    ----------
    cells : dict
        stores a particular record or row
    cooked : int
        stores a new compund object with a copy of a particular row or record.
    isEvaled : Bool
        it determines whether a y-value(dependent column value) is evaluated, if yes it is set to true
   
    """
    def __init__(self, t):
        
        self.cells = t
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False