





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


