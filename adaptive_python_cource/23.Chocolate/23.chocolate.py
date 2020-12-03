'''
Chocolate

A chocolate bar has a shape of rectangle, divided into NxM segments. You can break down this chocolate bar into two parts by a straight line. Find whether you can break off exactly K segments from the chocolate.

Input data format

The program gets an input of three integers: N, M, K

Output data format

The program must output one of the two words: YES or NO.



Sample Input 1:

4
2
6

Sample Output 1:

YES

Sample Input 2:

2
10
7

Sample Output 2:

NO



'''

def is_divider(large_a, small_b):
    if (large_a % small_b) == 0:
        return True
    

try:
    n = int(input().strip())
    m = int(input().strip())
    k = int(input().strip())
    
    if (is_divider(k, n) or is_divider(k, m)) and (n*m > k):
        print("YES")
    else:
        print("NO")
    
    
    
except:
    print('Your data is uncorrect')