s = 'hello world'
letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vowels = []
result = []
j = 0

for i in s:
    if i in letters:
        vowels.append(i)

vowels.reverse()

for i in s:
    if i in letters:
        result.append(vowels[j])
        j += 1
    else:
        result.append(i)

result = "".join(result)

print(result)