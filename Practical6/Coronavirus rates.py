dict={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
#This is the total number of COVID-19 cases on 11/3/21 for five countries
print(dict)

import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'USA','India','Brazil','Russia','UK'
sizes=[29862124,11285561,11205972,4360823,4234924]
explode=(0,0,0,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
		shadow=False,startangle=90)
plt.axis('equal')
# Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
