keys=['a','b','c','d','e']
values=[1,2,3,4,5]
mydict={k:v for (k,v) in zip(keys,values)}
print("using zip:",mydict)
keys.append(6)
print(keys)
mydict={x:x**2 for x in [1,2,3,4]}
print(mydict)
mydict={x:x+3 for x in range(1,10,5)}
print(mydict)
mydict={}