class Student(object):
	def __init__(self,first_name,last_name,undergraduate_programme):
		self.first_name=first_name
		self.last_name=last_name
		self.undergraduate_programme=undergraduate_programme
#To define a function which can print the Student List
a=input('first_name:      last_name:      undergraduate_programme:     ')
example=Student('Wen              ','Zhang            ','BMS')
#This is an example of my code
print(example.first_name,example.last_name,example.undergraduate_programme)







