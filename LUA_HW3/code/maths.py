def per(arr, p=0.5):
    x = len(arr)
    position = int(x*p +0.5)
    return arr[max(1,min(x, position))]