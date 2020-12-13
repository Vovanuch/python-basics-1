'''


Counting sort

The first line contains the number 1≤n≤104 1 \le n \le 10^4 1≤n≤104, the second one — n n n natural numbers, not exceeding 10. Output the sequence of these numbers sorted in a non-decreasing way.

Sample Input:

5
2 3 9 2 9

Sample Output:

2 2 3 9 9

'''

#try:
n = int(input().strip())
list_d = input().strip().split()

list_d_n = []
for i in range(n):
    list_d_n.append(int(list_d[i]))

list_d_n_sort = sorted(list_d_n)
list_d_n_sort_2 = [int(i) for i in list_d_n_sort]
print(*list_d_n_sort_2)
#except:
#    print('Incorrect input.')