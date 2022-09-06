
# ~ operator that flip positive number to negative
list=[1,3,21,2,9,0,3.3]
def medianFunc(list):
    list.sort()
    middle = len(list) // 2
    return (list[middle] + list[~middle]) / 2

x=medianFunc(list)
print(x)
 
#Working on STDEV
def mean(list): 
 return sum(list) / len(list) 
 
def stddev(list): 
 list_square = [x*x for x in list] 
 return (mean(list_square) - mean(list)**2)**.5 
 
print(mean(list), stddev(list))
