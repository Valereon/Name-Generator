import random

f = open("MythicalMetals.csv", "r")



Scoring = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
defualtScoreAlphabet = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

dicta = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
last3 = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
first3 = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
nameBeginning = []
nameMiddle = []
nameEnd = []

nameBeginningDict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
nameMiddleDict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
nameEndDict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

base = []
name = []




middlePercentage = []
begginingPercentage = []
endPercaentage = []

alphabet = list(dicta.keys())



def readinData():
    global base, middlePercentage, begginingPercentage, endPercaentage, namesNRatings
    namesNRatings = f.read().split("\n")

    for i in namesNRatings:
        for j in range(26):
            dicta[alphabet[j]] += i.count(alphabet[j])
        for x in range(3):
            last3[i[-3+x]] += 1
            first3[i[x]] += 1

    for i in range(26):
        middlePercentage.append(dicta[alphabet[i]]/len(namesNRatings))
        endPercaentage.append(last3[alphabet[i]]/len(namesNRatings))
        begginingPercentage.append(first3[alphabet[i]]/len(namesNRatings))
        base.append(middlePercentage[i] + endPercaentage[i] + begginingPercentage[i])
    print(base)
        
    
        
        
def generateName():
    # length = int(input("How long do you want the name to be?: "))
    length = 8
    endResult = []
    
    nameFinal = ""
    
    #randomly choose the first three letters the middle letters and the last 3 letters of the name and add them to the endResult
    endResult.append(random.choices(alphabet, weights=begginingPercentage, k=round(length/3)))
    endResult.append(random.choices(alphabet, weights=middlePercentage, k=round(length/4)))
    endResult.append(random.choices(alphabet, weights=endPercaentage, k=round(length/3)))
    for i in endResult:
        nameFinal += "".join(i)
        

        
    for i in nameFinal:
        for j in range(26):
            nameMiddleDict[alphabet[j]] += i.count(alphabet[j])
    #get the last and first 3 letters of the name
    for i in range(3):
        nameBeginningDict[nameFinal[i]] += 1
        nameEndDict[nameFinal[i-3]] += 1
    
    for i in range(26):
        nameBeginning.append(nameBeginningDict[alphabet[i]]/length)
        nameMiddle.append(nameMiddleDict[alphabet[i]]/length)
        nameEnd.append(nameEndDict[alphabet[i]]/length)
    
    
    
    for i in range(26):
        defualtScoreAlphabet[alphabet[i]] += nameMiddle[i] * .125
        defualtScoreAlphabet[alphabet[i]] += nameBeginning[i] * .25
        defualtScoreAlphabet[alphabet[i]] += nameEnd[i] * .25
    
    score = 0
    for i in range(26):
        score += defualtScoreAlphabet[alphabet[i]] * base[i]
    print(score)
    print(defualtScoreAlphabet)
    
    print("The Score of that name was: " + str(score))
    print(nameFinal)
    if(score < sum(Scoring.values())):
        generateName()
    else:
        print("Your name is: " + nameFinal)
        input("Press enter to Continue")
        for i in range(26):
            Scoring[alphabet[i]] = defualtScoreAlphabet[alphabet[i]]
        generateName()
    
        
    
    








def main():
    readinData()
    generateName()



main()









