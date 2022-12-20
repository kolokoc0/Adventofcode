subor = open("adofcode4.txt")
zoz = []
zoz2 =[]
poc = 0
for line in subor:
    line = line.strip("\n")
    pr1,pr2 = line.split(",")
    zoz = pr1.split("-")
    zoz2 = pr2.split("-")
    if int(zoz[0])<=int(zoz2[0]) and int(zoz[1])>=int(zoz2[1]):
        poc +=1
    elif int(zoz2[0])<=int(zoz[0]) and int(zoz2[1])>=int(zoz[1]):
        poc +=1
print(poc)
subor.seek(0)
zoz3=[]
zoz4=[]
poc1=0
temp = False
for line in subor:
    line = line.strip("\n")
    pr1,pr2 = line.split(",")
    zoz3 = pr1.split("-")
    zoz4 = pr2.split("-")
    for i in range(int(zoz3[0]),int(zoz3[1])+1):
        zoz3.append(i)
    for i in range(int(zoz4[0]),int(zoz4[1])+1):
        zoz4.append(i)
    zoz3 = set(zoz3)
    zoz4 = set(zoz4)
    intersection = zoz3.intersection(zoz4)
    intersection = list(intersection)
    if len(intersection)!=0:
        poc1+=1
        
print(poc1)