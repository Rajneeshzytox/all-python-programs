## STrings everything

# print(dir(str))
# methoods =  47
### pending ===>
# 'encode', 'expandtabs', 'format_map', ,
# 'maketrans', 'removeprefix', 'removesuffix',
# 'translate', 'zfill'

### complete ===>
# lower, capitalize, center, count, endswith, find, index, 'replace', split, strip, upper
# isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', isalnum, 'isalpha', 'isascii', 'isdecimal', 'isdigit'
# 'lstrip', 'rstrip', 'title', 'casefold', format, 'join', rfind', rsplit', rindex, partition, rpartition, startswith

#############################################################################################################

# a = 'hello wOoorLd'
# print(a[0])

# print("capitalize : ",a.capitalize())
# print("lower : ",a.lower())
# print("upper : ",a.upper())
# print("center : ",a.center(30, '-')) # => center ,
# print('hello'.ljust(30, '-')) # => ljust left-justified,
# print('hello'.rjust(30, '-')) # => rjust right-justified,
# print("count : ", a.count('o'))
# print("endswith world : ",a.endswith('world'))
# print("endswith wOoorLd : ",a.endswith('wOoorLd'))
# print("replace : ",a.replace('Ooo', '_'))


#### same func, find returns -1, and index throw valueError, when not found
# print("find O: ",a.find('k')) 
# print("index O: ",a.index('k')) 


# b = "hello my name, is something"
# print("split : ", b.split()) 
# print("split : ", b.split(',')) 
# print("split : ", b.split('is')) 


# c = "-g------------               hello my ---------- name, is something              -------------"
# print("strip :", c.strip('-'))


## IsAlnum
# print(help(str.isalnum))
## Return True if the string is an alpha-numeric string, False if other than alpha-num
# pswd = "abc4d"
# print("is alpha num: ", pswd.isalnum())
# print("pls enter char also") if pswd.isalnum() else print("ok")

## Is Digit
## print(help(str.isdigit))
## Return True if the string is a digit string, False otherwise.
##     A string is a digit string if all characters in the string are digits and there
##    is at least one character in the string.
# mobile = "12346f"
# print("is digit: ", mobile.isdigit())
# print("pls enter valid mobile num.") if (mobile.isdigit() == False) else print("ok")

### Is Identifier
### print(help(str.isidentifier))
## Return True if the string is a valid Python identifier, False otherwise.
## 'hello world' or 'hello%world' # => false
## 'hello_world' or 'class' # => true
# keywd = '_hello456'
# print("is keyword: ", keywd.isidentifier())


## isprintable
## print(help(str.isprintable))
## Return True if the string is printable, False otherwise.
## A string is printable if all of its characters are considered printable in repr() or if it is empty
# isprint = 'ÆæʤĠĦɥʛķĿŇŎʀʇüXŴż'
# print(f"is '{isprint}' pritable: ", isprint.isprintable())

## is title
## print(help(str.istitle))
## Return True if the string is a title-cased string, False otherwise.
## In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.
## The Fruits, The-Fruits, The_Fruits => true
## The fruits, the Fruits, The_fruits => false
# isTitle = 'The Fruits'
# print(f"is '{isTitle}' title: ", isTitle.istitle())

## is decimal
## print(help(str.isdecimal))
## 0b10, 0o10, 0x10, (2+0j), 7.5
# str1 = '56'
# print(f"is '{str1}' decimal: ", str1.isdecimal())

## lstrip, rstrip
# print(help(str.lstrip))
# print(help(str.rstrip))
# strip = '--------------        hello         -------------'
# print("strip left", strip.lstrip('-'))
# print("strip right", strip.rstrip('-'))

## titlr: Return a version of the string where each word is titlecased
# print(help(str.title))
# title_case = 'hello mY NamE iS Mr India'
# print(title_case.title())

## 'casefold': Return a version of the string suitable for caseless comparisons.
# print(help(str.casefold))
# caseStr = 'Hello WO rLd'
# print(caseStr.casefold())
# print(caseStr.lower())


# format: f"{variable}" or "{name}".format(name='raj')
# print(help(str.format))
# a = 'rajneesh '
# b = 67
# s = 'hello {1} {0}'
# print(s.format(a, b-2))

## Join
# print(help(str.join))
# a = 'hello'; b = 'world'; c = 'of'; d = 'python'
# print('_'.join([a,b,c,d]))

# rfind same as (index, find), but gives highest index
# rindex same as (index, find, rfind) but gives highest index

# rsplit', same to split but start from end to front.
# a = 'hello world of python'
# print(a.rsplit(maxsplit=2)) # => ['hello world', 'of', 'python']
# print(a.split(maxsplit=2))  # => ['hello', 'world', 'of python']


## partition and rpartition are same
# print(help(str.rpartition))
### returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.
# a = "hello world of py"
# print(a.partition('world'))
# print(a.rpartition('world'))

### swapcase
# print(help(str.swapcase))
### Convert uppercase characters to lowercase and lowercase characters to uppercase.
# a = 'hELLo WorlD'
# print(a.swapcase())

######################################################################





