from functools import reduce

def list_mult(lst):
    result = reduce(lambda x, y: x * y, lst)
    return result

nums = [2, 3, 4, 5]
result = list_mult(nums)
print(result)