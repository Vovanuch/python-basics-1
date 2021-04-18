'''


Given a sequence of natural numbers, not exceeding 30000. Find the sum of its elements, ending by 4. As input, the program gets the number of elements in the sequence, and then the elements themselves. In the sequence, there is always an element that ends by 4. The number of elements does not exceed 1000. The program should print the single number - the sum of elements in the sequence which ends by 4.

Sample Input:

6
4
19
96
14
44
20

Sample Output:

62

'''

n = int(input())
s = 0
for i in range(n):
    a = input()
    if a[-1] == '4':
        s += int(a)
        
print(s)