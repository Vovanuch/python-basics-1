''' import function with another name  '''

from imported_exception import BadName as bad, greeting as greet
import imported_exception as exc

def greeting(name='Bro'):
    print(f'I greet you, {name}!')
    
greeting()

greeting('Vladimir')

greet()

print('What is bad?', bad)
print('What is exc?', exc)
