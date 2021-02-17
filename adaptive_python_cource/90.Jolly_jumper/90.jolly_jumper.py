'''

The sequence of n>0 n \gt 0 n>0  integers is called a jolly jumper if the absolute differences of the consecutive elements take all the possible values between 1 1 1 and n−1 n-1 n−1.

For example, the sequence 1 -3 -4 -1 1 is a jolly jumper sequence, as the absolute differences are equal to 4 1 3 2, accordingly, and n−1=4 n-1 = 4 n−1=4.
We assume that a sequence containing only one element is a jolly jumper.

Write a program that checks whether the entered sequence is a jolly jumper.

Input format:
A string, containing 1≤n≤10000 1 \le n \le 10000 1≤n≤10000 space separated integers.

Output format:
One line, displaying "Jolly" (without quotation marks), if the sequence is a jolly jumper and "Not jolly" if otherwise.

Sample Input 1:

1 -3 -4 -1 1

Sample Output 1:

Jolly

Sample Input 2:

1 3 5

Sample Output 2:

Not jolly

Sample Input 3:

4

Sample Output 3:

Jolly

'''

list_n = [int(n) for n in input().strip().split()]
list_dif = []
for i in range(len(list_n) - 1):
    list_dif.append(abs(list_n[i+1] - list_n[i]))
#print(f'Current list of difs: {sorted(list_dif)}')

list_dif_etalon = [i for i in range(1, len(list_n))]
#print(f'Etalon list of difs: {list_dif_etalon}')

if sorted(list_dif) == list_dif_etalon:
    print("Jolly")
else:
    print("Not jolly")