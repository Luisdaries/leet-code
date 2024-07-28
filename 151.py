
# s = "the sky is blue"
# s = "  hello world  "
s = "a good   example"

array = (s.strip().split())

array.reverse()

array = " ".join(array)

print(array)