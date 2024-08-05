#sets
print("set methods")
myset={1,2,3,4,5,6}
print("myset:",myset)
originalset={4,5,6,7,8,9}
print("originalset:",originalset)
originalset=myset.copy()
print("after copied from the myset:",originalset)
originalset.clear()
print(originalset,"originalset cleared")
copiedset={4,5,6,7,8,9}
differenceset=myset.difference(copiedset)
print("difference set:",differenceset)
isdisjoint_set=myset.isdisjoint(copiedset)
print("isdisjoint_set:",isdisjoint_set)
issubset_set=myset.issubset(copiedset)
print("issubset_set:",issubset_set)
symmetricdifference_set=myset.symmetric_difference(copiedset)
print("symmetricdifference_set:",symmetricdifference_set)
union_set=myset.union(copiedset)
print("union_set",union_set)
myset.