from math import *

canh = []
for i in range (3):
	canh.append(int(input()))
canh.sort()

p = (canh[0] + canh[1] + canh[2]) / 2
S = sqrt(p*(p-canh[0])*(p-canh[1])*(p-canh[2]))
S = round(S,2)

if (canh[0] + canh[1] <= canh[2]):
	print('Khong phai tam giac')
elif canh[0] == canh[1] and canh[0] == canh[2]:
	print('Tam giac deu, dien tich =', S)
elif canh[0]*canh[0] + canh[1]*canh[1] == canh[2]*canh[2]:
	S = int(S)
	print('Tam giac vuong, dien tich =', S)
elif canh[1] == canh[2] or canh[0] == canh[1] or canh[2] == canh[0]:
	print('Tam giac can, dien tich =', S)
else:
	print('Tam giac thuong, dien tich =', S)
