#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing libraries
import pandas as pd #we import pandas library because we are going to work on our scatter plot
import numpy as np #numpy can execute a variety of mathematical operations on arrays
import matplotlib.pyplot as plt #matplotlib makes plots/low level graphs
import seaborn as sns #seaborn is a Matplotlib-based data visualization package, I use seaborn library to make colourfull graphs



#we are going to load the data we have called iris.data.csv using import cvs
#import csv
#file = open("iris.data.csv") #iris.data.csv is called the data frame we open
#csvreader = csv.reader(file) #we use the csvreader to read the file iris.data.csv
#header = next(csvreader) #'next' prints what's on a list or data file in order; returns to actual row then moves to the next row
#print(header) #we are printing what is in our file

#now we are extracting the rows
#rows = [] #we are defining an empty row
#for row in csvreader:  #we call the rows 
# rows.append(row) #we extract the rows
#print(rows) #we print the rows

#file.close() #we finish the operation

# generated text file function
def output_summary_txt():
    col=['sepal_length','sepal_width','petal_length','petal_width','type'] #col= colums; and we determine how to call what's in those colums 
    iris=pd.read_csv("iris.data.csv",names=col) #here we read the dataset iris.data.csv, 

    #output a summary of each variable to a text file
    summary_data = {"Summary Data": 'TotalAmount'}
    print(summary_data,  file=open('summarydata.txt', 'w'))



#Menu option 2
def output_histogram():
    col=['sepal_length','sepal_width','petal_length','petal_width','type'] #col= colums; and we determine how to call what's in those colums 
    iris=pd.read_csv("iris.data.csv",names=col) #here we read the dataset iris.data.csv, 

    #distribution of plots

    #below we are displaying the histogram of each type of Iris using the seaborn library: 

    #FacetGrid() class distributes a dataset onto several axes
    #shown in the form of a grid of rows/columns indicating the levels of variables in the dataset
    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"petal_length").add_legend() #FacetGrid is used here to distribute data

    plt.savefig("petal_lenght.png") #this is the code that saves each variable in our directory, we name the file and select what extension we want

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"petal_width").add_legend() #Hue is used to set a colour of subsets according to the type in our case
    plt.savefig("petal_width.png") #we save as png the histogram

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"sepal_length").add_legend() #with 'height' we determine the size of our histogram
    plt.savefig("sepal_lenght.png") #we save as pngthe histogram

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"sepal_width").add_legend()#histplot is a function that displays the histogram of data
    plt.savefig("sepal_width.png")#we save as png the histogram

    plt.show() #function used to show all open figures



def menu(): 
    print("[1] Save the summary data text")
    print("[2] Save histograms to png files")
    print("[3] Save scatter plot of variables")
    print("[4] Other analysis")
    print("[5] Exit the program")

menu() #we print the menu here
option = int(input("Enter your preference: ")) #I am getting the options from user

while option != 0:
    if option == 1:
        #enter option 1 thats in the menu
        output_summary_txt()
        pass
    elif option == 2:
        #enter option 2 that's in the menu
        output_histogram()
    
    
    else:
        print('Invalid input')
    print() #we are doing an empty print here
    menu()
    option = int(input("Enter your preference: "))

print("Thank you for using this program. Bye, Bye!")




#menu = {} #we are creating a menu
#menu['1']="See the summary of each variable" #inserting options point by point
#menu['2']="See petal lenght histogram"
#menu['3']="See petal width histogram"
#menu['4']="See sepal lenght histogram"
#menu['5']="See sepal width histogram"
#menu['6']="See optional histogram"
#menu['7']="See optional 1 histogram"
#menu['8']="Exit"




col=['sepal_length','sepal_width','petal_length','petal_width','type'] #col= colums; and we determine how to call what's in those colums 
iris=pd.read_csv("iris.data.csv",names=col) #here we read the dataset iris.data.csv, 



#here we are dividing in 3 parts the class data set
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"] #
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"] #
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"] #


    

#Scatter plot output


#Violin plot output

#Bloxplot output