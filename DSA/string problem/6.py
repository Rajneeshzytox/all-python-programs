# //String: Count the number of occurence of a char

str1 = 'Hello World of object oriented programming the python'


#--------------------------- list count
a = list(str1)
count = 0
char_to_count = 'o'
while(a.count(char_to_count)):
    count += 1
    a.remove(char_to_count)

print(f"{char_to_count} occured {count} times in string '{str1}'")
