tuple1 = ('physics','chemistry',1997,2000)
tuple2 = (1,2,3,4,5)
tuple3 = ("a","b","c","d")
tuple4 = ()
tuple5 = (50,)
list1 = [12,13,14,15]

print("tuple1[0]:",tuple1[0])
print("tuple2[1:] : ",tuple2[1:])
tuple2[2] = 6 # invalid 

del tuple1

print(len(1,2,3))
print((1,2,3)+(4,5,6))
print(("h!")*4)

3 in (1,2.3)

for x in tuple2:
    print(x)

print(max(tuple3))
print(min(tuple4))

list(tuple5)
tuple(list1)