class Student:
	def __init__(self, sid, grades):
	    self.sid = sid
	    self.grades = grades

	def __str__(self):
	    return "ID:"+self.sid + ', grades:' + str(self.grades)

	def __repr__(self):
	    return self.sid

	def __eq__(self, other):
	    return self.sid == other.get_sid()

	def set_sid(self, sid):
	    self.sid = sid

	def set_grades(self, grade):
	    self.grades = grades

	def get_sid(self):
	    return self.sid

	def get_grades(self):
	    return self.grades

	def add_grade(self, new_grade):
		self.grades.append(new_grade)

	def get_average(self):
		grades = self.get_grades()
		if len(self.grades) == 0:
			return 0
		sum = 0
		for g in self.get_grades():
			sum += g
		return sum / len(grades)
