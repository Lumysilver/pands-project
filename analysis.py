#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing libraries
import pandas as pd #we import pandas library because we are going to work on our scatter plot
import matplotlib.pyplot as plt #matplotlib makes plots/low level graphs, like the histograms we created and the scatter plot.
import seaborn as sns #seaborn is a Matplotlib-based data visualization package, I use seaborn library to make colourfull graphs.

# we are going to load the data we have called iris.data.csv using import cvs
col = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']    # we determine how to call what's in those iris.data.csv colums
iris = pd.read_csv("iris.data.csv", names = col) # here we read the dataset iris.data.csv

# define function that will save the summary data txt file - Menu option 1
def output_summary_txt(): # creates a new variable for each of iris types using groupby and get_group
    grouped = iris.groupby(iris.type)   #https://www.geeksforgeeks.org/split-pandas-dataframe-by-rows/
    setosa = grouped.get_group('Iris-setosa')
    versicolor = grouped.get_group('Iris-versicolor')
    virginica = grouped.get_group('Iris-virginica')

    f = open("summarydata.txt", "w")  # open or create a new txt file https://www.w3schools.com/python/python_file_write.asp
    # Iris-setosa data to be written in the summary text file
    f.write('Iris-setosa' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(setosa.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(setosa.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(setosa.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(setosa.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(setosa.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(setosa.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(setosa.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(setosa.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(setosa.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(setosa.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(setosa.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(setosa.petal_width.mean(), 2)) + '\n\n\n')
    # Iris-versicolor data to be written in the summary text file
    f.write('Iris-versicolor' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(versicolor.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(versicolor.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(versicolor.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(versicolor.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(versicolor.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(versicolor.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(versicolor.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(versicolor.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(versicolor.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(versicolor.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(versicolor.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(versicolor.petal_width.mean(), 2)) + '\n\n\n')
    # Iris-virginica data to be written in the summary text file
    f.write('Iris-virginica' + '\n' + '======================' + '\n')
    f.write('Sepal Length MIN: ' + str(min(virginica.sepal_length)) + '\n' + 'Sepal Length MAX: ' + str(max(virginica.sepal_length)) + '\n' + 'Sepal Length AVG: ' + str(round(virginica.sepal_length.mean(), 2)) + '\n')
    f.write('Sepal Width MIN: ' + str(min(virginica.sepal_width)) + '\n' + 'Sepal Width MAX: ' + str(max(virginica.sepal_width)) + '\n' + 'Sepal Width AVG: ' + str(round(virginica.sepal_width.mean(), 2)) + '\n')
    f.write('Petal Length MIN: ' + str(min(virginica.petal_length)) + '\n' + 'Petal Length MAX: ' + str(max(virginica.petal_length)) + '\n' + 'Petal Length AVG: ' + str(round(virginica.petal_length.mean(), 2)) + '\n')
    f.write('Petal Width MIN: ' + str(min(virginica.petal_width)) + '\n' + 'Petal Width MAX: ' + str(max(virginica.petal_width)) + '\n' + 'Petal Width AVG: ' + str(round(virginica.petal_width.mean(), 2)) + '\n\n\n')
    # close the file
    f.close()

#Menu option 2
def output_histogram():
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
   # create a new variable for each of iris types using groupby and get_group
    grouped = iris.groupby(iris.type)                       #https://www.geeksforgeeks.org/split-pandas-dataframe-by-rows/
    setosa = grouped.get_group('Iris-setosa')
    versicolor = grouped.get_group('Iris-versicolor')
    virginica = grouped.get_group('Iris-virginica')

    #https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/
    #https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html
    #iris setosa sepal and petal scatter plot
    plt.scatter(setosa.sepal_length, setosa.sepal_width, c ="grey", linewidths = 1, marker ="o", edgecolor ="green", s = 50)
    plt.scatter(setosa.petal_length, setosa.petal_width, c ="grey", linewidths = 1, marker ="s", edgecolor ="green", s = 50)
    #iris versicolor sepal and petal scatter plot
    plt.scatter(versicolor.sepal_length, versicolor.sepal_width, c ="grey", linewidths = 1, marker ="o", edgecolor ="red", s = 50)
    plt.scatter(versicolor.petal_length, versicolor.petal_width, c ="grey", linewidths = 1, marker ="s", edgecolor ="red", s = 50)
    #iris virginica sepal and petal scatter plot
    plt.scatter(virginica.sepal_length, virginica.sepal_width, c ="grey", linewidths = 1, marker ="o", edgecolor ="blue", s = 50)
    plt.scatter(virginica.petal_length, virginica.petal_width, c ="grey", linewidths = 1, marker ="s", edgecolor ="blue", s = 50)

    #Using pyplot to create visualizations
    #legend source: https://itsmycode.com/no-handles-with-labels-found-to-put-in-legend/
    #https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/scatter_with_legend.html
    plt.legend(("Setosa sepal", "Setosa petal", "Veriscolor sepal", "Veriscolor Petal", "Virginica sepal", "Virginica petal"), loc="upper left", title="Sizes")
    plt.xlabel("Length")
    plt.ylabel("Width")
    plt.title("Iris scatter plot") #https://stackoverflow.com/questions/42223587/plt-scatter-how-to-add-title-and-xlabel-and-ylabel
    plt.savefig('Iris_scatter.png')
    plt.show()
    
#Violin plot is usualy used to observe the density of data
#https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6
#https://stackabuse.com/matplotlib-violin-plot-tutorial-and-examples/
def violin_plot(): #we chosed this violin plot because we can observe the density better comparing with other plots
    sns.violinplot(x="type",y="petal_length",data=iris)
    plt.legend(("Setosa", "Veriscolor", "Virginica"), loc="upper left", fontsize = 10)
    plt.title("Iris Violin Plot")
    plt.savefig('Iris_Violin_Plot')
    plt.show()

    #define the user menu function and options
def menu(): 
    print("[1] Save the summary data text")
    print("[2] Save histograms to png files")
    print("[3] Save scatter plot of variables")
    print("[4] Save violin plot")
    print("[0] Exit the program")

menu() #we print the menu here
option = int(input("Enter your preference: ")) #getting the input from user
while option > 0: #using 'while elif' to generate what our user wants displayed from our menu
    if option == 1:
        #entered the option '1' on the menu
        output_summary_txt() #save the summary text file (summarydata.txt)
    elif option == 2:
        #enter option 2 that's in the menu
        output_histogram() #save histogram png 
    elif option == 3:
        #enter option 3 that's in the menu
        scatter_plot() #scatter plot
    elif option == 4: #the other analysis will be completed if I still time
        violin_plot()
    else:
        print('Invalid input') #any other input except for the ones above, will display the message 'invalid input'
    print() #we are doing an empty print here and ask again for an option
    menu()
    option = int(input("Enter your preference: "))
print('Thank you for using this program. Bye, Bye!') #if the user inserts '5' this message will be displayed