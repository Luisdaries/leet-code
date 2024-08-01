height = [1,8,6,2,5,4,8,3,7]

i = 0
j = len(height) - 1
array = []
while j > i:

    array.append((j - i) * (min(height[i], height[j])))

    if height[i] > height[j]:
        j = j - 1
    else:
        i = i + 1

print(max(array))
