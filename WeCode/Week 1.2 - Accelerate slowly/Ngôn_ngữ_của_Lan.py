arr=str(input()).split(' ')
check=True
checkGT=True

def Solve(arr):
    GT=-1
    TS=1
    newTS=-1
    sumGT=0
    countNoun=0
    for i in range(len(arr)):
        GT=-1
        newTS=-1
        s1=arr[i][-3:]
        s2=arr[i][-4:]
        s3 = arr[i][-5:]
        s4=arr[i][-6:]
        if s2=="lios":
            newTS=1
            GT=0 
        if s3=="liala":
            newTS=1
            GT=1
        if s1=='etr':
            newTS=2
            GT=0
            countNoun+=1
        if s2=='etra':
            newTS=2
            GT=1
            countNoun+=1
        if s4=='initis':
            newTS=3
            GT=0
        if s4=='inites':
            newTS=3
            GT=1
        if GT==-1:
                return False
        else:
            sumGT+=1
        if  GT==-1:
            return False
        if countNoun>=2:
            return False
    if len(arr)>=2 and countNoun!=1:
        return False 
    if sumGT==0 or sumGT==len(arr):
        return True 
    return False

s=Solve(arr)
if s==True:
    print("YES")
else:
    print("NO")
