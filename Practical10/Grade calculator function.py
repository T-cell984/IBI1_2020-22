class information(object):
	def __init__(self,student_name,portfolio,presentation,exam):
		self.student_name=student_name
		self.portfolio=portfolio
		self.presentation=presentation
		self.exam=exam
	def grade(self):		
		code=(int(self.portfolio))*40/100
		poster=(int(self.presentation))*30/100
		final=(int(self.exam))*30/100
		print(code+poster+final)
a=input('student_name:     portfolio    ,presentation       ,exam')
example=information('Wen Zhang         ','80            ' ,'80               ','80')
#This is an example of my code
print(example.student_name,example.portfolio,example.presentation,example.exam)
print(information.grade(example))
#To calculate the final mark of the student
