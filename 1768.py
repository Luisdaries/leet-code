# word1 =  "abc"
# word2 = "pqr"

word1 = "ab"
word2 = "pqrs"
#
# word1 =  "abcd"
# word2 = "pq"
array = []

wordmax = word1 if len(word1) > len(word2) else word2
wormin = word1 if len(word1) < len(word2) else word2


for i in range(len(wordmax)):

    if len(word1) > i :

        array.append(word1[i])

        if len(word2) > i :
            array.append(word2[i])

    else:
        array.append(word2[i])

        if len(word1) > i :
            array.append(word1[i])


string_list = ''.join(array)
print(string_list)