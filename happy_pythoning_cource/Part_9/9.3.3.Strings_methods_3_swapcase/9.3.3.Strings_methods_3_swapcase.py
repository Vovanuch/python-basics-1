'''

sWAP cASE

На вход программе подается строка. Напишите программу, которая меняет регистр символов, другими словами замените все строчные символы заглавными и наоборот.

Формат входных данных 
На вход программе подается строка.

Формат выходных данных
Программа должна вывести строку в соответствии с условием задачи.

Sample Input 1:

Swap Case

Sample Output 1:

sWAP cASE

Sample Input 2:

Www.sTepik.com

Sample Output 2:

wWW.StEPIK.COM

Sample Input 3:

Pythonist 2

Sample Output 3:

pYTHONIST 2

'''

s = input().strip()
print(s.swapcase())