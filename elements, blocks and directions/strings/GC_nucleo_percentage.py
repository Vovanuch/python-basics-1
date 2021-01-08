#percentage of G and C in nucleo-order

print("Enter your nucleo sequence:")
s = input()

g = s.upper().count("G")
c = s.upper().count("C")
gc = g + c

#pgc - percentage of G and C
pgc = (gc / len(s))*100
print(pgc)
