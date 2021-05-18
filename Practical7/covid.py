import os
import pandas as pd
covid_data=pd.read_csv("full_data.csv")
#to import the .csv file
print(covid_data.head(11))
print(covid_data.info())
print(covid_data.describe())
#to show all columns and every second row between (and including) 0 and 10
my_columns = [False, False, False, False, True, False]
print(covid_data.iloc[1:82,my_columns])
#use a Boolean to show "total_cases" for all rows corresponding to Afghanistan

import numpy as np
A=pd.read_csv("world_new_cases.csv")
a=np.array(A)
b=np.mean(a)
print(b)
#this is the mean of new cases for the entire world
c=np.median(a)
print(c)
#this is the median of new cases for the entire world

import matplotlib.pyplot as plt
plt.boxplot(a)
plt.ylabel('world new cases')
plt.title('New cases worldwide')
plt.show()
#to create a boxplot of new cases worldwide

B=pd.read_csv("world_new_deaths.csv")
plt.plot(A,B,'r-')
plt.ylabel('world new deaths')
plt.xlabel('world new cases')
plt.title('New cases vs new deaths worldwide')
plt.show()
#this is a figure which plots both new cases and new deaths worldwide

C=pd.read_csv("China_new_cases.csv")
D=pd.read_csv("China_new_deaths.csv")
plt.ylabel('China new deaths')
plt.xlabel('China new cases')
plt.plot(C,D,'b+')
plt.title('New cases vs new deaths in China')
plt.show()
#the code to answer the question 





