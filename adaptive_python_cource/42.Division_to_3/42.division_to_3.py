'''


You are given an integer number of indefinite length. Check, whether this number divides by 3 or not, without using the remainder (%) operation.

Print "YES" if the number divides by 3 and "NO" if it doesn't.

Note: What happens, when you divide, say, 17 by 3? And then back.

Sample Input 1:

7

Sample Output 1:

NO

Sample Input 2:

43

Sample Output 2:

NO

Sample Input 3:

18

Sample Output 3:

YES

'''

def check_3(n):
    # a = n // 3
    if (n//3)*3 == n:
        print("YES")
    else:
        print("NO")


try:
    check_3(int(input().strip()))
    
    
except:
    print('Incorrect input')