#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing libraries that will help with the data set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #


#we are going to load the data we have called iris.data using import cvs
#data is called the data frame we have
import csv
file = open("iris.data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()


col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.data.csv",names=col)

#now we print the shape and size of the iris(references in read me file)
print("First five rows")
print(iris.head())
print("*********")
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each type") 
print(iris["type"].value_counts())
print("*********")
print(iris.describe())

#here we are dividing in 3 parts the class data set
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

#distribution plots
#below we are displaying the plot of each type of Iris
#sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"petal_length").add_legend()
#sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"petal_width").add_legend()
#sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"sepal_length").add_legend()
#sns.FacetGrid(iris,hue="type",size=3).map(sns.distplot,"sepal_width").add_legend()
#plt.show()


#Violin plot example, we plot violin plot of our iris data:
#sns.violinplot(x="type",y="petal_length",data=iris)
#plt.show()

#BoxPlot plot display for petal lenght:
sns.boxplot(x="type",y="petal_length",data=iris)
plt.show()

#BoxPlot plot display for petal width:
sns.boxplot(x="type",y="petal_width",data=iris)
plt.show()

#BoxPlot plot display for petal lenght:
#sns.boxplot(x="type",y="sepal_lenght",data=iris)
#plt.show()

#BoxPlot plot display for petal lenght:
#sns.boxplot(x="type",y="sepal_width",data=iris)
#plt.show()