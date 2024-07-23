nums = [1,5,0,4,1,3]
# nums = [9,10,5,11,10,9,8]
# nums = [14,22,21,11,90]

first_min = float('inf')
second_min = float('inf')

for num in nums:
    if num <= first_min:
        first_min = num
    elif num <= second_min:
        second_min = num
    else:
        print(True)
