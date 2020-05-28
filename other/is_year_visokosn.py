#Високосные и обычные года.
Year = int(input())
#vYear = Year % 400
if ( ( (Year % 4 == 0) and (Year % 100)!=0 ) or ((Year % 400)==0) and (Year>=1900 and Year <=3000) ):
    print("Високосный")
else:
    print("Обычный")
