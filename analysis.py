#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing different libraries
import pandas as pd #we import pandas library because we are going to work on our scatter plot
import numpy as np #numpy can execute a variety of mathematical operations on arrays
import matplotlib.pyplot as plt #matplotlib makes plots/low level graphs
import seaborn as sns #seaborn is a Matplotlib-based data visualization package
from sklearn import datasets


#we are going to load the data we have called iris.data.csv using import cvs
import csv
file = open("iris.data.csv") #iris.data.csv is called the data frame we have to open
csvreader = csv.reader(file) #we use the csv.reader to read the csv file
header = next(csvreader) #we are extracting the field names
print(header) #we are printing the header

#now we are extracting the rows
rows = [] #we are defining an empty row
for row in csvreader:  #we call the rows 
    rows.append(row) #extract the rows
print(rows) #we now print
file.close() #we finish the operation


col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.data.csv",names=col)


#here we are dividing in 3 parts the class data set
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

#Scatter plot output



#distribution plots
#below we are displaying the plot of each type of Iris using seaborn library
def new_func(iris):
   sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"petal_length").add_legend() 
   sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"petal_width").add_legend()
   sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"sepal_length").add_legend()
   sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"sepal_width").add_legend()
   plt.show()



#below we have a series of ways to create a plot with violin plot and boxplot for the other type of analysis I will create

#Violin plot example, we plot violin plot of our iris data:
#sns.violinplot(x="type",y="petal_length",data=iris)
#plt.show()

#BoxPlot plot display for petal lenght:
#sns.boxplot(x="type",y="petal_length",data=iris)
#plt.show()

#BoxPlot plot display for petal width:
#sns.boxplot(x="type",y="petal_width",data=iris)
#plt.show()

#BoxPlot plot display for petal lenght:
#sns.boxplot(x="type",y="sepal_lenght",data=iris)
#plt.show()

#BoxPlot plot display for petal lenght:
#sns.boxplot(x="type",y="sepal_width",data=iris)
    #plt.show()

new_func(iris)