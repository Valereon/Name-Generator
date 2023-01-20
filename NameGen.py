import random as r
#                                                  GENERATING NAMES
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
probOfLettersAsNameGoesOn = [ [0] * 26] * 12
letterPairIndex = []
letterPairss = []

f = open("Data/justTheNames.csv", "r")
fi = f.read().split("\n")



def generateData():   
    #calculating probabilities
    for nameIndex in range(len(fi)):
        for slotNum in range(len(fi[nameIndex])):
            char = fi[nameIndex][slotNum]
            probOfLettersAsNameGoesOn[slotNum][alphabet.index(char)] += 1    
        print("Generating Data: " + str(round(nameIndex / len(fi) * 100, 2)) + "%", end="\r")
    print("Generating Data: 100%")



    #normalizing probabilities
    for slotnum in range(len(probOfLettersAsNameGoesOn)):
        for letter in range(len(probOfLettersAsNameGoesOn[slotnum])):
            probOfLettersAsNameGoesOn[slotnum][letter] = probOfLettersAsNameGoesOn[slotnum][letter] / sum(probOfLettersAsNameGoesOn[slotnum]) * 100
        print("Normalizing Data: " + str(round(slotnum / len(probOfLettersAsNameGoesOn) * 100, 2)) + "%", end="\r")
    print("Normalizing Data: 100%")
    


#list of all the letter pairs and their index in the name
def letterPairs():    
    global letterPairss, letterPairIndex, finalList, finalListNum
    print(letterPairIndex)
    for j in range(len(fi)):
        for i in range(len(fi[j])-1):
            #get the two chars next to each other
            letterPairss.append(fi[j][i] + fi[j][i+1])
            letterPairIndex.append(i)
        print("Generating Data: " + str(round(j / len(fi) * 100, 2)) + "%", end="\r")
    print("Generating Data: 100%")
    

    letterPairss, letterPairIndex = zip(*sorted(zip(letterPairss, letterPairIndex)))

    removed = list(set(letterPairss))
    removed.sort()


    finalList = []
    finalListNum = [[0] * len(removed)] * max(letterPairIndex)


    for pair in letterPairss:
        if finalList.count(pair) == 0:
            finalList.append(pair)
        for i in range(len(finalList)):
            if pair == finalList[i]:
                finalListNum[letterPairIndex[letterPairss.index(pair)]][i] += 1


     #normalizing probabilities
    for slotnum in range(len(finalListNum)):
        for letter in range(len(finalListNum[slotnum])):
            finalListNum[slotnum][letter] = finalListNum[slotnum][letter] / sum(finalListNum[slotnum]) * 100


    print(finalList)
    print(finalListNum)


def GenerateName(amount):
    global rFinal
    #for each name to be generated run this loop
    for slotnum in range(amount):
        doubleOrNot = [finalList,alphabet]



        
        final = r.choices( r.choice(doubleOrNot), weights=probOfLettersAsNameGoesOn[0],  k=1)
        final += r.choices(r.choice(doubleOrNot), weights=finalListNum[1],  k=1)
        final += r.choices(r.choice(doubleOrNot), weights=finalListNum[2],  k=1)
        final += r.choices(r.choice(doubleOrNot), weights=finalListNum[3],  k=1)
        rFinal = ""
        #take the list elements and add them to a string
        for i in final:
            rFinal += i
        print(rFinal)
    


def main():
    global rFinal
    generateData()
    letterPairs()
    amount = None

    while amount != 0:
        amount = int(input("How many names do you want?(0 to exit):"))        
        GenerateName(amount)

main()