''' вложенные словари '''

dic = {'global':{'parent':'None', 'vars':[]}}
print(dic)
#dic.update('ns1':{'parent':'global', 'vars':[]})
dic['ns1'] = {}
dic['ns1'] = {'parent':'global', 'vars':[]}
print(dic)
