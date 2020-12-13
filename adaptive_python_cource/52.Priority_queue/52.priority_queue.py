'''


Priority Queue

The first input line contains the number of operations 1≤n≤105 1 \le n \le 10^5 1≤n≤105. Each of the following n n n lines define the operation of one of the following types:

    Insert {\tt Insert} Insert x {\tt x} x, where 0≤x≤109 0 \le x \le 10^9 0≤x≤109 — integer number;
    ExtractMax {\tt ExtractMax} ExtractMax.

First operation adds number x x x to the priority queue, the second one extracts the maximum number and outputs it.

Sample Input:

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:

200
500

'''

import heapq

n = int(input().strip())

# create list of commands
list_commands = []
for i in range(n):
    list_commands.append(input().strip().split())

list_nums = []
for i in list_commands:
    if i[0] == 'Insert':
        heapq.heappush(list_nums, -int(i[1]))
        #list_nums.append(int(i[1]))
        #heapq.heapify(list_nums)
        #print(list_nums)        
    if i[0] == 'ExtractMax':
        #print(max(list_nums))
        #list_nums.remove(max(list_nums))
        print(-heapq.heappop(list_nums))
        
#print(list_nums)
