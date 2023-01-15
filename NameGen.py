import random as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer






# e = open("endings.csv", "r")



# e = e.read().split(",")
# print(e)




#       TRAINING DATA
# df = pd.read_csv("Base.csv")

# train, test = train_test_split(df, test_size=0.2, random_state=42)



# trainX, trainY = train["Names"], train["Ratings"]
# testX, testY = test["Names"], test["Ratings"]



# tfidf = TfidfVectorizer(stop_words="english")
# trainXVector = tfidf.fit_transform(trainX)
# testXVector = tfidf.transform(testX)



# #           SVC MODEL
# from sklearn.svm import SVC
# svc = SVC(kernel="linear")
# svc.fit(trainXVector, trainY)


##          NAIVE BAYES
# from sklearn.naive_bayes import GaussianNB
# gnb = GaussianNB()
# gnb.fit(trainXVector.toarray(), trainY)

# #        logistic REGRESSION
# from sklearn.linear_model import LogisticRegression
# log_reg = LogisticRegression()
# log_reg.fit(trainXVector, trainY)

# #       DECISION TREE
# from sklearn.tree import DecisionTreeClassifier
# dec_tree = DecisionTreeClassifier()
# dec_tree.fit(trainXVector, trainY)





# #       SCORING 
# print(svc.score(trainXVector, trainY))
# print(dec_tree.score(trainXVector, trainY))
# print(gnb.score(trainXVector.toarray(), trainY))
# print(log_reg.score(trainXVector, trainY))



# # F1 SCORE
# from sklearn.metrics import f1_score
# print(f1_score(testY, svc.predict(testXVector), labels=[0,1], average=None))



# #       PREDICTION
# print(svc.predict(tfidf.transform(["Aarav"])))
# print("THIS IS DADS NAME BELOW")
# print(svc.predict(tfidf.transform(["Amakey"])))
# predict = svc.predict(testXVector)
# print(predict)
# print(testX)

# goodNames = []


# for i in range(len(predict)):
#     if predict[i] == 1:
#         goodNames.append(testX.iloc[i])


# for i in goodNames:
#     print(i)
    
    



#                                                  GENERATING NAMES
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# a list of 26x12 of probabilities
probOfLettersAsNameGoesOn = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



def generateData():
    #reading in data
    f = open("justTheNames.csv", "r")
    fi = f.read().split("\n")
    #COUNTING OF LETTERS AS THEY GO ATTEMPT 3.0 WITH SPENCERS HELP 
    #SUCCESS
    for nameIndex in range(len(fi)):
        for slotNum in range(len(fi[nameIndex])):
            char = fi[nameIndex][slotNum]
            probOfLettersAsNameGoesOn[slotNum][alphabet.index(char)] += 1         

    for slotnum in range(len(probOfLettersAsNameGoesOn)):
        for letter in range(len(probOfLettersAsNameGoesOn[slotnum])):
            probOfLettersAsNameGoesOn[slotnum][letter] = probOfLettersAsNameGoesOn[slotnum][letter] / sum(probOfLettersAsNameGoesOn[slotnum]) * 100



final = ""
def GenerateName(amount):
    global rFinal
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
        for i in final:
            rFinal += i
        print(rFinal)
    









def main():
    global rFinal
    generateData()
    f = open("Base.csv", "a")
    while True:
        amount = int(input("How many names do you want?(0 to exit):"))
        if amount == 0:
            break
        GenerateName(amount)
        yesNo = input("Do you like these names? Y/N if you dont have an opinion press enter...").lower()
        if yesNo == "y" or yesNo == "yes":
            f.write(rFinal + "," + "1" + "," + "\n")
        elif yesNo == "n" or yesNo == "no":
            f.write(rFinal + "," + "0" + ","+ "\n")
        else:
            pass
    f.close()


main()




        


# #       PREDICTING NAMES
# amount = int(input("How many names do you want?:"))
# length = int(input("How long do you want the names to be?:"))

# nameCount = 0
# finalName = ""
# while nameCount < amount:

#     svc.predict(tfidf.transform([finalName]))
#     print(svc.predict(tfidf.transform([finalName])))
#     print(finalName)
#     if svc.predict(tfidf.transform([finalName])) == 1:
#         print(finalName)
#         nameCount += 1


