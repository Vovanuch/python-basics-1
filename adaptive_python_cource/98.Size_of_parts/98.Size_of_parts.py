'''


A detector compares the size of parts produced by a machine with the reference standard. 

If the size of the part is larger, it can be sent to be fixed, and the detector prints the number 1.
If the size of the part is smaller, it is removed as reject, and the detector prints the number -1.
If the part was made perfect, it is sent to the box with ready products, and the detector prints 0.

Write a program, which takes the number of parts n as input, and then the sequence of detector prints. The program should output numbers in a single line – the number of ready parts, the number of parts to be fixed, and the number of rejects.

Sample Input:

10
-1
1
0
-1
1
-1
1
1
-1
0

Sample Output:

2 4 4

'''
n = int(input().strip())
list_n = []
for i in range(n): 
    list_n.append(int(input().strip()))
print(list_n.count(0), list_n.count(1), list_n.count(-1))