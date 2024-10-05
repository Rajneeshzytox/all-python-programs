# print(dict)
# print(dir(dict))
### Methods
#  'fromkeys', 'update'
# complete: 
# 'clear', 'copy', 'get', 'items', 'keys', 'values', 'setdefault', 'pop', 'popitem',

# roll_no = [1: 65, 2: 66, 3: 67, 4: 68] # wrong 
# roll_no = {1: 65, float(7+7): 66, (4,5,6): 67, 'name': 68, hex(16): 685, None: 78, False: 90, True: 99} # correct
# not valid keys type: list, sets, dict
# true dont show print(roll_no[True]) gives value (99)
# print(roll_no)

###########################################################################

# 1. clear()
# roll_no.clear()
# print(roll_no)

## 2. copy()
# a = {'a': 'apple', 'b': "banana", 'c': 'cat'}
# b = a.copy()
# c = a
# print("a ", id(a), a)
# print("b ", id(b), b)
# print("c ", id(c), c)
# print(f" a is b : {a is b}\n a is c : {a is c}")

# # 3. keys()
# a = {'a': 'apple', 'b': "banana", 'c': 'cat'}
# print(a.keys()) # dict_keys(['a', 'b', 'c'])

# 4. get 
# a = {'a': 'apple', 'b': "banana", 'c': 'cat'}
# print(a.get('b'))
# print(a['b'])

## 5 items
# print(help(dict.items))
# a = {'a': 'apple', 'b': "banana", 'c': 'cat'}
# print(a.items())
# x, y, z = a.items()
# print(x, y, z)
# for x,y in a.items():
#     print(f"val of {x} is {y} ")

## 6. values : gives only values
# print(help(dict.values))
# a = {'a': 'apple',  'b': "banana", 'c': 'cat'}
# print(a.values())
# output :  dict_values(['apple', 'banana', 'cat'])

## 7. setdefault
# print(help(dict.setdefault))
# a = {'a': 'apple',  'b': "banana", 'c': 'cat'}
# b = a.setdefault(5, 'dfh')
# print(b)
# print(a)


## 8.  pop 
# print(help(dict.pop))
# a = {'a': 'apple',  'b': "banana", 'c': 'cat'}
# b = a.pop('a', 'not available')
# # b = a.pop('f') # ====> keyError
# # b = a.pop('f', 'not available')
# print(b)

# 9.  popitems: last element remove, returns a tuple ()
# print(help(dict.popitem))
# a = {'a': 'apple',  'b': "banana", 'c': 'cat'}
# a.popitem()
# a.popitem(0) ==> error 
# print(a) 


#------------------------------------------------------------------------------------------
"""
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)

"""