
elements = [
    ("a", 1, "aneeraj"),
    ("b", 2, "x"),
    ("c", 1, "niharika"),
    ("a", 1, "lata"),
    ("a", -5, "lata5"),
    ("a", 5, "lata5")
    ]



sort_compare = lambda  x : x

print(sorted(elements, key= sort_compare))

'''
if a == b : return 0 // which mains both values
if a < b :
  return -1
else 1 // a > b
'''