import random as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

    
    



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
    df = pd.DataFrame({"Letter Pair": letterPairss, "Index": letterPairIndex})
    print(df.head(5))
    for i in range(11):
        df.insert(0,i,0)
    for i,r in df.iterrows():
        df.at[i, r["Index"]] += 1
    print(df)



    

    




    
    
    
    # for index, rows in df.iterrows():
    #     #count the number of times the letter pair appears in the dataframe
    #     count = df[df.columns(index)].str.count([df.columns(index)])
    #     print(count)
    #     df.at[index, "Count"] += count[index]
    # #Copy the finished data to a new dataframe
    # finished = df.groupby(by="Letter Pair")["Count"].sum()
    # print(finished.head(5))
    



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
        
        #decision tree for writing to file
        yesNo = input("Do you like these names? Y/N if you dont have an opinion press enter...").lower()
        if yesNo == "y" or yesNo == "yes":
            data.write(rFinal + "," + "1" + "," + "\n")
        elif yesNo == "n" or yesNo == "no":
            data.write(rFinal + "," + "0" + ","+ "\n")
        else:
            pass
    f.close()


# main()




        
