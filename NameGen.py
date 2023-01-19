import random as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#                                                  GENERATING NAMES
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# a list of 26x12 of probabilities for every letter in a a spot in an 8 letter name
probOfLettersAsNameGoesOn = [ [0] * 26] * 12
#letter pair chart



#list of 4x325 of probabilities for each letter pair in a 8 letter name, Currently not used, using a pandas Dataframe instead
letterPairIndex = []
letterPairss = []
# probOfLetterPairs = [[0] * 325] * 4


#reading in data
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
    
# generateData()

#list of all the letter pairs and their index in the name
def letterPairs():    
    global letterPairss, letterPairIndex
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

    print(finalList)
    print(finalListNum)

        






    #                            Failed Attempts 1.0
    # for letterP in range(len(letterPairss)):
    #     if letterP == len(letterPairss) - 1 :
    #             break
    #     for slot in range(len(finalListNum)):
    #         if letterP == len(letterPairss) - 1:
    #             break
    #         if letterPairss[letterP] == letterPairss[letterP + 1]:
    #             if letterPairIndex.count(letterPairIndex[letterP]) > 1:
    #                 finalList.append(letterPairss[letterP])
    #             if letterPairIndex[letterP] == letterPairIndex[letterP + 1]:
    #                 print(letterP)
    #                 print(slot)
    #                 try:
    #                     finalListNum[letterP][slot] += 1
    #                 except IndexError:
    #                     print("IndexError")
    #                 
    # 
    # 
                #   Another Failed Attempt 2.0
    # for letterP in range(len(letterPairss)):
    #     for slot in range(len(letterPairIndex)):
    #         if letterP == len(letterPairss):
    #             break
    #         if finalList.count(letterPairIndex[letterP]) == 0:
    #             finalList.append(letterPairss[letterP])
    #         char = letterPairss[letterP]
    #         if letterPairss[letterP] == letterPairss[letterP + 1]:
    #             if letterPairIndex[letterP] == letterPairIndex[letterP + 1]:
    #                 finalListNum[letterP][finalList.index(char)] += 1
    # print(finalListNum)

             
             
             
            # if letterPairss[letterP] == letterPairss[letterP + 1]:
            #     print(letterPairIndex[letterP])
            #     if letterPairIndex[letterP] == letterPairIndex[letterP]:
            #         finalListNum[letterP][slot] += 1
                    
           

    
    
    
                            # Failed Attempt 3.0 using dataframes
    # going away from the pandas dataframe method, it was too complicated
    # df = pd.DataFrame({"Letter Pair": letterPairss, "Index": letterPairIndex})
    # print(df.head(5))
    # z = 0
    # finalList = []
    # finalListNum = []
    # for i in range(817):
    #     df.insert(0,i,0)
    # for i,r in df.iterrows():
    #     df.at[i, r["Index"]] += 1
    #     if i == len(df) - 1:
    #         break
    #     z = i
    #     if df.loc[z, "Letter Pair"] == df.loc[z + 1, "Letter Pair"]:
    #         if df.loc[z,"Index"] == df.loc[z + 1, "Index"]:
    #             print("reached")
    #             finalList.append(df.loc[i, "Letter Pair"])
    #             print(finalList)
                
    #             z = i
    #             while df.loc[z, "Index"] == df.loc[z + 1, "Index"]:
    #                 if  df.loc[z, "Letter Pair"] == df.loc[z + 1, "Letter Pair"]:
    #                     df.loc[z, r[z]] += 1
    #                     z += 1
    #                     if z == len(df) - 1:
    #                         print("break")
    #                         break
    #                 else:
    #                     break
    #                 finalListNum.append(df.loc[i, r[i]])

    # print(finalList)
    # print(finalListNum)
    # finalList, finalListNum = zip(*sorted(zip(finalList, finalListNum)))
    # print(finalList)
    # print(finalListNum)

            
    



    

    






letterPairs()





def GenerateName(amount):
    global rFinal
    #for each name to be generated run this loop
    for slotnum in range(amount):
        final = r.choices(alphabet, weights=probOfLettersAsNameGoesOn[0], k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[1],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[2],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[3],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[4],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[5],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[6],k=1)
        final += r.choices(alphabet, weights=probOfLettersAsNameGoesOn[7],k=1)
        rFinal = ""
        #take the list elements and add them to a string
        for i in final:
            rFinal += i
        print(rFinal)
    









def main():
    global rFinal
    #generate the data for name generation
    generateData()
    
    #while user dosent want to exit
    while True:
        
        #how many names to generate
        amount = int(input("How many names do you want?(0 to exit):"))
        #if its zero exit
        if amount == 0:
            break
        
        GenerateName(amount)

# main()




        
