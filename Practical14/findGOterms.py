import re
from xml.dom.minidom import parse
import xml.dom.minidom
def find(i,term):
#to define a function which can find whether there is a sequence in the parent node defstr or not
    is_a = []
    flag = False
    is_a = term.getElementsByTagName('is_a')
    if is_a == []:
        flag = False
    else:
        for a in is_a:
            parentid = a.childNodes[0].data
            s = re.findall(':(\d.*)$',parentid)
            digitid = int(s[0])
            fatherterm = terms[loc[digitid]]
            defstr = fatherterm.getElementsByTagName('defstr')[0]
            d = defstr.childNodes[0].data
            if re.search(i,d):
                flag = True
            elif find(i,fatherterm):
                flag = True
    return flag
go_obo = open('go_obo_file.xml','r')
DOMTree = xml.dom.minidom.parse('go_obo_file.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')      

DNA=RNA=protein=carbohydrate=j=0 
loc = [0]*10000000

for term in terms:
    termid = term.getElementsByTagName('id')[0].childNodes[0].data
    p = re.findall(':(\d.*)$',termid)
    q = int(p[0])
    loc[q] = j
    j = j+1
for term in terms:
    if find('DNA',term):
        DNA = DNA+1
print(DNA)
#this is the number of childNodes associated with 'DNA'
for term in terms:
    if find('RNA',term):
        RNA = RNA+1
print(RNA)
#this is the number of childNodes associated with 'RNA'
for term in terms:
    if find('protein',term):
        protein = protein+1
print(protein)
#this is the number of childNodes associated with 'protein'
for term in terms:
    if find('carbohydrate',term):
        carbohydrate = carbohydrate+1
print(carbohydrate)
#this is the number of childNodes associated with 'carbohydrate'

import os
import matplotlib.pyplot as plt 
#Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'DNA-associated\n'+str(DNA),'RNA-associated\n'+str(RNA),'protein-associated\n'+str(protein),'carbohydrate-associated\n'+str(carbohydrate)
sizes = [DNA,RNA,protein,carbohydrate]
explode=(0,0.1,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes, explode=explode, labels=labels,autopct='%1.2f%%', 
        shadow=True,startangle=90)
plt.axis('equal')
#Equal aspect ratio ensures that pie is drawn as a circle
plt.title('The number of childNodes associated with macromolecules')
plt.show()
#this is a pie chart describing the number of childNodes associated with each of these terms
