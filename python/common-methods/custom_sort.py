from collections import Counter
elements = [
    ("a", 1, "aneeraj"),
    ("b", 2, "x"),
    ("c", 1, "niharika"),
    ("a", 1, "lata"),
    ("a", -5, "lata5"),
    ("a", 5, "lata5")
    ]



# pass tuple if sorting needs to be done on basis on multiple params.
# Next parameter will only be considered if values equal for previous parameter
sort_compare = lambda  x : (x[1], x[0])

print(sorted(elements, key= sort_compare, reverse=True))

'''
if a == b : return 0 // which mains both values
if a < b :
  return -1
else 1 // a > b
'''

# s = "leetcode"
# freq_map = Counter(s)
# s_list = list(s)
# s_list.sort(key=lambda x:freq_map[x], reverse=True)
# print("".join(s_list))
# sorted_list = sorted(s, key= lambda x: -1*freq_map[x])
# result = "".join(sorted_list)
# print(result)