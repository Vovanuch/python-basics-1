''' Список как value in dict '''
dic = {}
rows = []
print('Enter count of rows')
n = int(input())
for i in range(n):
    rows.append(input().strip().split())
    
print('rows:',rows)

j = 0
for i in rows:
    dic[j] = i
    j += 1

dic[0] += [1, 2, 3]
print('dic: ',dic)
