'''


Write the function update_dictionary(d, key, value), which takes the dictionary d d d and the two numbers key key key and value value value.

If the key key key key is present in the dictionary d d d, then append the value value value value to the list, which is stored by this key.
If the key key key key is not present in the dictionary, you need to append the value to the list keyed 2⋅key 2⋅key 2⋅key. Is there is no key 2⋅key 2\cdot key 2⋅key, you need to add the key 2⋅key 2\cdot key 2⋅key to the dictionary and store the list [value] [value] [value] by it.

You need to implement only this function, there should be no code except of it.
The function should not call the input and print functions.

An example of how function works:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

'''

def update_dictionary(d, key, value):
    #d1 = {}
    #d_k = d.keys()
    #d_v = d.values()
    
    if (key in d.keys()):
        d[key].append(value)
    else:
        if (2*key in d.keys()):
            d[2*key].append(value)
        else:
            d[2*key] = [value]
    
    return d

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}