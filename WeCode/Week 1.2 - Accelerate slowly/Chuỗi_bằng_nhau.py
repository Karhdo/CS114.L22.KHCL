n = int(input())
def Check(str1, str2):
    for i in range(len(str1)):
        if str1[i] in str2: 
        	return "YES"
    return "NO"
for i in range(n):
    a = str(input())
    b = str(input())
    print(Check(a,b))
