#n is the number of IBI1 students and also the number of infected students
n=84
#r is the number of infected individuals afer 5 rounds of infection for a given rate
r=1
#a,b,c,d,e are the total number of individuals infected afer 1,2,3,4,5 generations
a=n*r+n
b=a*r+a
c=b*r+b
d=c*r+c
e=d*r+d
print(e)
