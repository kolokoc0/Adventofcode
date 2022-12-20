subor = open("adofcode6.txt","r")
poc = 0
str = ""
for i in subor:
    for a in i:
        if len(str)!=14: #Zmenil som namiesto 4 na 14 pri druhej casti
            str +=a
            poc+=1
        else:
            str = str.replace(str[0],"",1)
            str+=a
            poc+=1
            a = set(str)
            if len(a)==14:
                print(poc)
                break