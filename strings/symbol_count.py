# подсчёт количества определённого символа в строке

s = input("Enter your string: ")
c = input("Enter needed symbol (only one, please!): ")

j = 0
for i in s:
	if i == c:
		j += 1
			
print ("We find that symbol", j, "times")
