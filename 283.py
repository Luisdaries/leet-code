"""
Do not return anything, modify nums in-place instead.
"""

# nums = [0,1,0,3,12]
# nums = [0]
nums = [0,0,1]

contador = 0

array = []
for num in nums:
    if num == 0:
        contador += 1
    else:
        array.append(num)

for i in range(contador):
    array.append(0)

for i in range(len(nums)):
    nums[i] = array[i]

print(nums)