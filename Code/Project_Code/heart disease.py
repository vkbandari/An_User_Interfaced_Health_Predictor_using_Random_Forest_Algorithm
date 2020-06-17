import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import itertools


df = pd.read_csv("heart.csv")

col = ["age","sex","chest_pain","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","diagnosis"]

df.columns = col #assigning the column name

df_x = df.drop("diagnosis", axis = 1) #independent variables
df_y = df["diagnosis"] #target variable

for index,val in enumerate(df_y):
    if val>0:
        df_y[index] = 1


#lets see the percentage count for person with and without heart disease in our dataset
positive = len(df_y[df["diagnosis"]==1])/len(df_y)
negative = len(df_y[df["diagnosis"]==0])/len(df_y)

print("Positive = %0.2f , Negative = %0.2f" %(positive,negative))


#lets view the correlation in feature dataset
plt.figure(figsize= (12,8))
sns.heatmap(df_x.corr(), cmap = "Blues", linewidth = '0.5', annot = True)

#woowww! all the attributes seems independent

#so now lets view the correlation between each attributes and target variable
correlation = []
p_value = []
for column in df_x.columns:
    cor, p_val = spearmanr(df_x[column], df_y)
    correlation.append(cor)
    p_value.append(round(p_val,2))

#lets plot now
y_pos = np.arange(len(df_x.columns))
plt.figure(figsize = (12,8))
plt.bar(y_pos,correlation)
plt.xticks(y_pos,df_x.columns, rotation = 270)
plt.title("Correlation Bar plot")

#from correlation plot it is very clear that "fbs" is not significant but lets see its effect on model

#lets select our model from random forest, logisticRegression, and SVC
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import GridSearchCV,train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression as LR
from sklearn.svm import SVC
#lets prepare our training and testing dataset
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y, test_size = 0.3, random_state = 42)

clf = RFC(random_state = 12)
clf1 = LR(random_state = 42)
clf2 = SVC(random_state = 12, kernel = 'linear')
#lets see our model performance  without tunning the parameters then we will build our model on which ever parameter gives the best result

for classifier, label in zip([clf,clf1,clf2], ["Random Forest","LogisticRegression","SVM"]):
    #calculating cross validation score
    score = cross_val_score(classifier,x_train,y_train, cv = 7, scoring = "accuracy")
    
    print(f"Accuracy from {label} is {score.mean()}")

#So Logistic Regression proves to give better accuracy but we know that regression model are good to use only when we want to predict value in\from range so to overcome that and to build better model for prediction lets go for random froest as that too gives a good accuracy

#lets perfrom gridsearch cross-validation for Random Forest to find the best model
    
param = {"max_depth":[5,10,15],
         "n_estimators":[10,15,20,25,30,40,50],
         "max_features":[2,3,4],
         "min_samples_leaf":[3,4,5],
         "min_samples_split":[2,3,4,5],
         "bootstrap":[True]}

grid = GridSearchCV(estimator = clf, param_grid = param, cv = 7, verbose = 3)

grid.fit(x_train,y_train)

cv_keys = ("mean_test_score","std_test_score","params")


for k,_ in enumerate(grid.cv_results_["mean_test_score"]):
    print(f"{grid.cv_results_[cv_keys[0]][k]} , {grid.cv_results_[cv_keys[1]][k]}, {grid.cv_results_[cv_keys[2]][k]}")

print(f"Best score : {grid.best_score_}")
print(f"Best Param : {grid.best_params_}")

clf = RFC(random_state= 21,bootstrap= True, max_depth= 5, max_features= 3, min_samples_leaf= 3, min_samples_split= 2, n_estimators=25)
clf.fit(x_train,y_train)
pred = clf.predict(x_test)

accuracy = accuracy_score(pred,y_test)

print(f"Accuracy on Test dataset = {round(accuracy,2)}")

#defining function for confusion matrix
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    See full source and example: 
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    

#assigning labels to "y_test" and "pred"
pred = pred.astype(object)
for i,row in enumerate(pred):
    if row == 0:
        pred[i] = "Negative"
    else:
        pred[i] = "Positive"

for index in y_test.index:
    if y_test[index] == 0:
        y_test[index] = "Negative"
    else:
        y_test[index] = "Positive"


labels = ["Positive", "Negative"]
 
cm = confusion_matrix(pred,y_test,labels)

plot_confusion_matrix(cm,classes =["Positive", "Negative"] )


















