def count_positives_sum_negatives(arr):
    if not arr: return []
    positive_number = 0
    negative_number = 0
    for x in arr:
        if x > 0:
            positive_number += 1
        elif x < 0:
            negative_number += x
            
    return [positive_number, negative_number]
  