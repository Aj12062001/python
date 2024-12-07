import math
import random
nums = []
for i in range(10):
    nums.append(math.floor(random.random() * 10))
print(f'Old list: {nums}')
new_nums = []
for i in range(0,len(nums)):
    if (nums[i]%2 != 0):
        new_nums.append(nums[i])
print(f'\nnew list without even numbers: {new_nums}')
