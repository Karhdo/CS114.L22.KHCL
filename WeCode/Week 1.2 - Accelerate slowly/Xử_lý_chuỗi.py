string = input()
string = str.lower(string)

string = string.replace('a','')
string = string.replace('o','')
string = string.replace('y','')
string = string.replace('e','')
string = string.replace('u','')
string = string.replace('i','')

lenght = len(string)

for i in range(lenght):
	if(i == lenght-1):
		print('.' + string[i])
	else:
		print('.' + string[i], end='')
