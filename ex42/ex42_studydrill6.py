#demonstrating is-many relationship using multiple inheritance.

#a university_person who is-a instructor and a student at the same time 
class instructor(object):
	def __init__(self, name):
		self.name = name
		
	def work(self, subject):
		print "%s is an instructor on subject %s" %(self.name, subject)
		

class student(object):
	def __init__(self, name):
		self.name = name
		
	def work(self, subject):
		print "%s the student is studying the subject %s" %(self.name, subject)
		
#multiple inheritance
class university_person(student, instructor):

	def __init__(self, name):
		super(university_person, self).__init__(name)
		
	
mary = university_person("Mary")
#the first mentioned parent class is taken as the parent class of the university_person
mary.work("Mathematics")
