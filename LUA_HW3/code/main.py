import misc
import sys
sys.path.append(sys.path[0]+'\\..\\tests\\')
import testEngine

if __name__ == "__main__":
    obj = misc.CLI()
    print(misc.the,"From main class line 8")
    testEngine.runs(misc.the["eg"])