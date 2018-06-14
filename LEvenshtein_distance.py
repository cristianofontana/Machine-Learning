def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

##############################

ruasCorretas = ['Marechal Deodoro','Av. Sete de Setembro']
teste = ["Mal Deodoro","M Deorodo","Marechal Deldoro"]

#y = 0 
#for ruas in ruasCorretas:
#    print (ruasCorretas[y])
#    for test in teste:
#        x = 0
#        print (minimumEditDistance(ruasCorretas[y],teste[x]))
#        x = x + 1
#    y = y+1

x = 0 
for test in teste:
    print(' ')
    print (teste[x])
    print(' ')
    y = 0
    for ruas in ruasCorretas:
        print (str(minimumEditDistance(ruasCorretas[y],teste[x]))+" - "+ruasCorretas[y])
        y = y+1
    x = x+1
