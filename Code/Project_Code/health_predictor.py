import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("c:\\Users\\Ritesh\\Downloads\\disease_train.csv").drop('Unnamed: 0', axis = 1)

#lets 1st difine our independent and target variable

df_x = df.drop('prognosis', axis = 1)
df_y = df['prognosis']

#lets factorize our target variable

factor = pd.factorize(df_y)
df_y = factor[0] #factorizing out target variable
defination = factor[1] #storing our difination for the factors


#lets dive deep into data for EDA perpective for a while
a4dim = (8.5,6)
fig, ax = plt.subplots(figsize = a4dim)
sns.countplot(df['prognosis'], label = 'Prognosis')

fig, ((a,b), (c,d)) = plt.subplots(2,2,figsize = a4dim)
sns.set(font_scale = 1.5)
sns.countplot(df['prognosis'], hue = df.iloc[:,1], ax = a)  
sns.countplot(df['prognosis'], hue = df.iloc[:,2], ax = b)  
sns.countplot(df['prognosis'], hue = df.iloc[:,3], ax = c)  
sns.countplot(df['prognosis'], hue = df.iloc[:,4], ax = d)  



#lets train our model on Random forest
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.linear_model import LogisticRegression as lr
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(df_x,df_y, test_size = 0.3, random_state = 42)



clf = RFC(random_state = 123)
clf1 = lr()
clf2 = SVC()

for classifier,label in zip([clf,clf1,clf2],["RFC","Logistic Regression", "SVM"]):
    score = cross_val_score(classifier, x_train,y_train, cv = 5, scoring = 'accuracy')
    
    print(f"Acccuracy from {label} is {np.mean(score)}")
    
    
#lets use RandomForest

clf.fit(x_train,y_train)

pred = clf.predict(x_test)

accuracy = accuracy_score(pred, y_test)    
    
    
    
    
    
    
    
    