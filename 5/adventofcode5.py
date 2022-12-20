subor = open("adofcode5.txt","r")
list = [["F","R","W"],["P","W","V","D","C","M","H","T"],["L","N","Z","M","P"],["R","H","C","J"],["B","T","Q","H","G","P","C"],["Z","F","L","W","C","G"],["C","G","J","Z","Q","L","V","W"],["C","V","T","W","F","R","N","P"],["V","S","R","G","H","W","J"]]
#list = [["N","Z"],["D","C","M"],["P"]]
num = []
for line in subor:
    line = line.strip("\n").split(" ")
    for i in line:
        if i.isdigit():
            i = (int(i)-1)
            num.append(i)
    for a in range(0,(num[0])+1): 
            c = list[num[1]].pop(0)
            list[num[2]].insert(0,c)
    num = [ ]
print(list)
subor.seek(0)
num2 = []
#list2 = [["N","Z"],["D","C","M"],["P"]]
list2 = [["F","R","W"],["P","W","V","D","C","M","H","T"],["L","N","Z","M","P"],["R","H","C","J"],["B","T","Q","H","G","P","C"],["Z","F","L","W","C","G"],["C","G","J","Z","Q","L","V","W"],["C","V","T","W","F","R","N","P"],["V","S","R","G","H","W","J"]]
for line in subor:
    line = line.strip("\n").split(" ")
    for i in line:
        if i.isdigit():
            i = (int(i)-1)
            num2.append(i)
    if num2[0]+1 != 1:
        for a in range((num2[0]),-1,-1):
            c = list2[num2[1]].pop(a)
            list2[num2[2]].insert(0,c)
    else:
        for a in range(0,(num2[0])+1): 
            c = list2[num2[1]].pop(0)
            list2[num2[2]].insert(0,c)
    num2 = [ ]
print(list2)



