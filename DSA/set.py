# print("type of set is ", type(set))

# for i in dir(set):
#     if (i.startswith('__') == True):
#        continue
#     print(i, end=', ') 

# Methods: 
# add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, symmetric_difference_update, union, update,

# ------------------------------------------------------------------------------------------------------
a = {1,2,3,4,5,5}
# print("type of ",a, "is : ", type(a))
# for i in a:
#     print(i)
# print(a[0])  # ===> TypeError: 'set' object is not subscriptable



# ------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
###### print(help(set))
"""
 |  add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |------------------------------------------------------------------------------------------------------
 |  clear(...)
 |      Remove all elements from this set.
 |------------------------------------------------------------------------------------------------------
 |  copy(...)
 |      Return a shallow copy of a set.
 |------------------------------------------------------------------------------------------------------
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |------------------------------------------------------------------------------------------------------
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |------------------------------------------------------------------------------------------------------
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      Unlike set.remove(), the discard() method does not raise
 |      an exception when an element is missing from the set.
 |------------------------------------------------------------------------------------------------------
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |
 |      (i.e. all elements that are in both sets.)
 |------------------------------------------------------------------------------------------------------
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |------------------------------------------------------------------------------------------------------
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |------------------------------------------------------------------------------------------------------
 |  issubset(self, other, /)
 |      Test whether every element in the set is in other.
 |------------------------------------------------------------------------------------------------------
 |  issuperset(self, other, /)
 |      Test whether every element in other is in the set.
 |------------------------------------------------------------------------------------------------------
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |------------------------------------------------------------------------------------------------------
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |------------------------------------------------------------------------------------------------------
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |------------------------------------------------------------------------------------------------------
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |------------------------------------------------------------------------------------------------------
 |  union(...)
 |      Return the union of sets as a new set.
 |
 |      (i.e. all elements that are in either set.)
 |------------------------------------------------------------------------------------------------------
 |  update(...)
 |      Update a set with the union of itself and others.
 ------------------------------------------------------------------------------------------------------
 
 """