import misc
import sys
from testEngine import runs

if __name__ == "__main__":
    obj = misc.Misc()
    arg_len = len(sys.argv)
    if arg_len > 1:
        if sys.argv[1] == "-e":
            runs(sys.argv[2])
