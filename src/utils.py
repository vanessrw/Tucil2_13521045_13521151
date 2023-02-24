# median without sorting (divide n conquer)

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return select(arr, n // 2)
    else:
        return (select(arr, n // 2 - 1) + select(arr, n // 2)) / 2
 
def select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return select(highs, k - len(lows) - len(pivots))
