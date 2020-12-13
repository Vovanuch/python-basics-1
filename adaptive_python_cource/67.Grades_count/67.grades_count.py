'''


Find the number of "Ds", "Cs", "Bs" and "As" for the last test on informatics in the class consisting of n students. The program gets number n as input, and then gets the grades themselves (one by one). The program should output four numbers in a single line - the number of "D", the number of "C", the number of "B" and the number of "A" grades.

Sample Input:

14
3
4
5
3
3
4
3
3
3
2
4
2
3
3

Sample Output:

2 8 3 1

'''

def get_scores(n):
    list_scores = []
    for i in range(n):
        list_scores.append(int(input().strip()))
    return list_scores

n = int(input().strip())
list_scores_all = get_scores(n)
list_scores_uniq = sorted(list(set(list_scores_all)))

for i in list_scores_uniq:
    print(list_scores_all.count(i), end=' ')