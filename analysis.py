#I will start the research on the data set online and write a summary
# Download the data set and add it to my repository.
#Research what data libraries will help me achieve the results I want; 

#importing libraries that will help with the data set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#we are going to load the data we have called iris.data using import cvs
#that loads tha data right into a panda data frame
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

