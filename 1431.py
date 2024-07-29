# candies = [2,3,5,1,3]
# extraCandies = 3


# candies = [4,2,1,1,2]
# extraCandies = 1


candies = [12,1,12]
extraCandies = 10


result = []
for candie in candies:
    if max(candies) <= candie + extraCandies:
        result.append(True)
    else:
        result.append(False)

print(result)