#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing libraries
import filecmp
from tkinter import W
import pandas as pd #we import pandas library because we are going to work on our scatter plot
import numpy as np #numpy can execute a variety of mathematical operations on arrays
import matplotlib.pyplot as plt #matplotlib makes plots/low level graphs
import seaborn as sns #seaborn is a Matplotlib-based data visualization package, I use seaborn library to make colourfull graphs
import plotly.graph_objects as px #scatter plot library

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

    # we determine how to call what's in those iris.data.csv colums
    col = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']

    # here we read the dataset iris.data.csv
    iris = pd.read_csv("iris.data.csv", names = col) 

    # create a new variable for each of iris types using groupby and get_group
    grouped = iris.groupby(iris.type)          #https://www.geeksforgeeks.org/split-pandas-dataframe-by-rows/
    setosa = grouped.get_group('Iris-setosa')
    versicolor = grouped.get_group('Iris-versicolor')
    virginica = grouped.get_group('Iris-virginica')
    
    # open or create a new txt file
    f = open("summarydata.txt", "w")      #https://www.w3schools.com/python/python_file_write.asp

    # Iris-setosa data to be writed in the summary text file
    f.write('Iris-setosa' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(setosa.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(setosa.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(setosa.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(setosa.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(setosa.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(setosa.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(setosa.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(setosa.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(setosa.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(setosa.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(setosa.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(setosa.petal_width.mean(), 2)) + '\n\n\n')

    # Iris-versicolor data to be writed in the summary text file
    f.write('Iris-versicolor' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(versicolor.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(versicolor.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(versicolor.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(versicolor.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(versicolor.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(versicolor.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(versicolor.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(versicolor.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(versicolor.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(versicolor.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(versicolor.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(versicolor.petal_width.mean(), 2)) + '\n\n\n')
    
    # Iris-virginica data to be writed in the summary text file
    f.write('Iris-virginica' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(virginica.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(virginica.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(virginica.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(virginica.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(virginica.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(virginica.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(virginica.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(virginica.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(virginica.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(virginica.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(virginica.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(virginica.petal_width.mean(), 2)) + '\n\n\n')
    
    # close the file
    f.close()



#Menu option 2
# define function that will save the summary data txt file - Menu option 2
def output_histogram():
    #distribution of plots

    #below we are displaying the histogram of each type of Iris using the seaborn library: 

    #FacetGrid() class distributes a dataset onto several axes
    #shown in the form of a grid of rows/columns indicating the levels of variables in the dataset
    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"petal_length").add_legend() #FacetGrid is used here to distribute data

    plt.savefig("petal_lenght.png") #this is the code that saves each variable in our directory, we name the file and select what extension we want

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"petal_width").add_legend() #Hue is used to set a colour of subsets according to the type in our case
    plt.savefig("petal_width.png") #we save as png the histogram

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"sepal_length").add_legend() #with 'height' we determine the size of our histogram
    plt.savefig("sepal_lenght.png") #we save as png the histogram

    sns.FacetGrid(iris,hue="type",height=5).map(sns.histplot,"sepal_width").add_legend()#histplot is a function that displays the histogram of data
    plt.savefig("sepal_width.png")#we save as png the histogram

    plt.show() #function used to show all open figures


## define function that will generate the scatter plot - Menu option 3
def scatter_plot():

 











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
    elif option == 3:
        #enter option 3 that's in the menu
        print 
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
# creating random data through randomint
# function of numpy.random
np.random.seed(42)
 
random_x= np.random.randint(1,101,100)
random_y= np.random.randint(1,101,100)
 
plot = px.Figure(data=[px.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',)
])
                  
plot.show()


#Violin plot output


#Bloxplot output