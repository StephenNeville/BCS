# A functional approach to squaring
# a list of numbers
# The function sqr is passes as a argument to the map function
# In this case: map(a function,  to each element of a list of numbers)
# The function list appends each element to a new list
# comprising each of the elements of nums which are squared

nums = [1,2,4,5,7]

def sqr(nums): return nums ** 2

print(list(map(sqr, nums)))

# The output will be 
# [1, 4, 16, 25, 49]
