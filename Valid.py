s = input("First Word : ").lower()
t = input("Second Word : ").lower()
sList = []
tList = []
for i in s:
    sList.append(i)
for i in t:
    tList.append(i)
sList.sort()
tList.sort()
if sList == tList:
    print("True")
else:
    print("False")
