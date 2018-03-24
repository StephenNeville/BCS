# A functional approach to squaring
# a list of numbers

nums = [1, 2, 3, 4, 5]

def sqr(nums): return nums ** 2

print(list(map(sqr, nums)))

# The output will be 
# [1, 4, 16, 25, 49]
