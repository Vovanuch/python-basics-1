'''
str funcs
'''

str1 = "  1 \t 2 3 4 5      "
list1 = str1.split()
print(list1)
str2 = "  *  1 \t 2 3 4 5   *   "
print(str2.split.__doc__)
list2 = str2.split(" * ")
print(list2)

str3 = "  *  1 \t 2 3 4 5   *   "
str3.strip()
print(str3.split())

str4 = "  *  1 \t 2 3 4 5   *   "
str4 = str4.lstrip("* ")
print(str4)
str4 = str4.rstrip("* ")
print(str4)
str4 = str4.strip("* ")
print(str4)
print(str4.split())