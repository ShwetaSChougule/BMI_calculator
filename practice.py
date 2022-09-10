l1 = ['a','b','c','d']

obj1 = enumerate(l1,start=0)
print(list(obj1))

l2 = [2,2,3,4,5]
o = enumerate(l1)
a = list(o)
print(a[0])

# mmultiple ip
n = map(int,(input('enter data')).split())   #map(fun,iter)
print(list(n))