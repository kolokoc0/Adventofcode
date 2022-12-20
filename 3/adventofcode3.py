subor= open("adofcode3.txt","r")
str1 = ""
str2 = ""
sum = 0
let = ""
for line in subor:
    line.strip()
    str1 = set(str1 + line[:(len(line))//2:])
    str2 = set(str2 + line[(len(line))//2::])
    let = str1.intersection(str2)
    for i in let:
        if i.isupper():
            sum += (ord(i)-64+26)
        else:
            sum += (ord(i)-96)
    str1,str2 ="","" 
print(sum)
subor.seek(0)
sum1=0
end = 0
inter =""
inter2 =""
for line in subor:
    line = line.strip()
    line = set(line)
    if end==0:
        firstline = line
        end+=1
    elif end ==1:
        inter = firstline.intersection(line)
        end+=1
    elif end==2:
        inter2 = inter.intersection(line)
        end ==0
        for i in inter2:
            if i.isupper():
                sum1 += (ord(i)-64+26)
                end = 0
            else:
                sum1 += (ord(i)-96)
                end = 0
print(sum1)


    
    




