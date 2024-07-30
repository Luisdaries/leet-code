# chars = ["a","a","b","b","c","c","c"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","a","a"]


def validate(position1, position2):
    if position1 == position2:
        return position1 == position2


contador = 1
array = []

for i in range(len(chars) - 1):

    if validate(chars[i], chars[i + 1]):
        contador += 1
    else:
        array.append(chars[i])
        if contador > 1:
            array.extend(list(str(contador)))
        contador = 1

array.append(chars[-1])
if contador > 1:
    array.extend(list(str(contador)))

chars.clear()
chars.extend(array)

print(chars)