import os
os.chdir("C:/Users/张雯/IBI1_2020-21/Practical7")
print(os.getcwd())
print(os.listdir())
import pandas as pd
covid_data=pd.read_csv("full_data.csv")
print(covid_data.head(11))
print(covid_data.info())
print(covid_data.describe())
my_columns = [False, False, False, False, True, False]
print(covid_data.iloc[1:82,my_columns])
import numpy as np
A=pd.read_csv("world_new_cases.csv")
a=np.array(A)
b=np.mean(a)
print(b)
c=np.median(a)
print(c)
import matplotlib.pyplot as plt
plt.boxplot(a)
plt.ylabel('world new cases')
plt.show()
B=pd.read_csv("world_new_deaths.csv")
plt.plot(A,B,'r-')
plt.ylabel('world new deaths')
plt.xlabel('world new cases')
plt.show()

C=pd.read_csv("China_new_cases.csv")
D=pd.read_csv("China_new_deaths.csv")
plt.plot(C,D,'b+')
plt.ylabel('China new deaths')
plt.xlabel('China new cases')
plt.show()
#to show China new cases and new deaths



