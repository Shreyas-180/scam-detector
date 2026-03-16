import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB # using because of many words(columns) in the matrix
from sklearn.feature_extraction.text import CountVectorizer # makes matrix made of each word
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import  Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.linear_model import LogisticRegression
import pickle

clf1 = Pipeline([('vectorizer',CountVectorizer()),('nb',MultinomialNB())]) # bayes naive
clf2 = Pipeline([('vectorizer',CountVectorizer()),('rf',RandomForestClassifier(n_estimators= 70))])
clf3 = Pipeline([('vectorizer',CountVectorizer()),('lr',LogisticRegression())])
clf4 = Pipeline([('vectorizer',TfidfVectorizer()),('nb',MultinomialNB())]) # isnt that good
df = pd.read_csv('data/modified.csv')
X = df['Message']
y = df['Spam']
# a = cross_val_score(clf1,X,y, cv = 5).mean()
# b = cross_val_score(clf2,X,y, cv = 5).mean()
# c = cross_val_score(clf3, X,y, cv = 5).mean()

X_train,X_test,y_train,y_test = train_test_split(X,y)
# clf.fit(X_train,y_train)
metrics = ['accuracy', 'precision', 'recall']
scores1 = cross_validate(clf1, X, y, cv=5, scoring=metrics)
scores2 = cross_validate(clf2, X, y, cv=5, scoring=metrics)
scores3 = cross_validate(clf3, X, y, cv=5, scoring=metrics)
scores4 = cross_validate(clf4, X, y, cv=5, scoring=metrics)
clf1.fit(X, y) # training on whole data set before saving
clf2.fit(X,y)
clf3.fit(X,y)
clf4.fit(X,y)
with open('bayes_model_tfidf.pkl','wb') as file:
    pickle.dump(clf4,file)
# with open('randomforest_model.pkl','wb') as file1:
#     pickle.dump(clf2,file1)
# with open('logisticregression_model.pkl','wb') as file2:
#     pickle.dump(clf3,file2)


#print("bayes: ",a,"random forest classifier: ",b,"logistic regression: ",c)
print("--- Naive Bayes ---")
print("Accuracy:  ", scores1['test_accuracy'].mean())
print("Precision: ", scores1['test_precision'].mean())
print("Recall:    ", scores1['test_recall'].mean())
print("\n--- Random Forest ---")
print("Accuracy:  ", scores2['test_accuracy'].mean())
print("Precision: ", scores2['test_precision'].mean())
print("Recall:    ", scores2['test_recall'].mean())
print("\n--- Logistic Regression ---")
print("Accuracy:  ", scores3['test_accuracy'].mean())
print("Precision: ", scores3['test_precision'].mean())
print("Recall:    ", scores3['test_recall'].mean())
print("--- Naive Bayes TfIdf ---")
print("Accuracy:  ", scores4['test_accuracy'].mean())
print("Precision: ", scores4['test_precision'].mean())
print("Recall:    ", scores4['test_recall'].mean())

# print(df.head())

# print(df.describe())