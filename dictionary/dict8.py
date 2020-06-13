''' nested dictionary '''

info = {'TEST' : {'name' : 'Lida', 'age' : 30}} 
   
 
print("The Input dictionary: " + str(info)) 
   
 
info['TEST']['Address'] = 'Pune'
   
 
print("Dictionary after adding key to nested dict: " + str(info)) 
print()
###
info['test2'] = {}
info['test2'] = {'name' : 'Vova', 'age' : 33}
print(str(info))
