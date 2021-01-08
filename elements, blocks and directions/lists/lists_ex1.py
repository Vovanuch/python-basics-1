''' list exsiding '''
def list_ex1(lst1, lst2):
    lst2 = lst1 + lst2
    return lst2
    
    
def list_ex2(lst1, lst2):
    lst2[0:0] = lst1
    return lst2



l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'b']
l3 = list_ex1(l1, l2)
print(*l3)

l3 = []
l3 = list_ex2(l2, l1)
print(*l3)
