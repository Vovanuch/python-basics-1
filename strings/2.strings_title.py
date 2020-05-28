#2. Как проверить то, что каждое слово в строке начинается с заглавной буквы?

#Существует строковый метод istitle(), который проверяет, начинается ли каждое слово в строке с заглавной буквы.

print( 'The Hilton'.istitle() ) #=> True
print( 'The dog'.istitle() ) #=> False
print( 'sticky rice'.istitle() ) #=> False
