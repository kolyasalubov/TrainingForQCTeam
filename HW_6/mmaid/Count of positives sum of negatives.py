def count_positives_sum_negatives(arr):
    b = []
    c = 0
    for i in arr:
        if i > 0:
            b.append(i)
        else:
            c += i
    return [len(b), c] if arr != [] else [] 
