from django.db import models
#from django import forms #i don't actually know what this does and I don't ahve internet so just going with it.
#from numpy import percentile
from scipy import stats
import math
import functools



class Institution(models.Model):
#this is the university. allows for inclusion of other schools if you're interested.
	name = models.CharField(max_length = 255)
	def __unicode__(self):
		return self.name

class Campus(models.Model):
	name = models.CharField(max_length = 255)
	institution = models.ForeignKey(Institution)
	def __unicode__(self):
		return self.name

class College(models.Model):
	name = models.CharField(max_length = 255)
	campus = models.ForeignKey(Campus)
	#code = models.CharField(max_length = 5)
	total_budget = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
      #self.sector = self.get_sector()
		super(College, self).save(*args, **kwargs)

class Department(models.Model):
	name = models.CharField(max_length=255)
	college = models.ForeignKey(College)
	total_budget = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)

class Organization(models.Model):
	name = models.CharField(max_length=255)
	department = models.ForeignKey(Department)
	total_budget = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)

class Position(models.Model):
	title = models.CharField(max_length = 255)
#	TYPE_CHOICES = (
		#Forget the terms. Civil service vs ... salaried?
#		('Salaried', 'Salaried'),
#		('Hourly', 'Hourly')
#		)
#	job_type = models.CharField(max_length = 20, choices = TYPE_CHOICES)
	def __unicode__(self):
		return self.title

	def average_salary(self):
#		salaries = Employee.objects.filter(position = self)
		stats = {}
		#return all the fuckers I can gather here.
		return stats
#consult payday. Is the work done by the server in this case on the histograms. basically, what does the bucketing?

#The grey book lists the person every fucking time. OH GOD. I have to work in the superclasses. 
#fuck. me. 

class EmployeeSuper(models.Model):
	name = models.CharField(max_length = 255)
	def __unicode__(self):
		return self.name

class Employee(models.Model):
	#there are some similar names...
	identity = models.ForeignKey(EmployeeSuper)
	year = models.IntegerField(default = 0)
	present_total_FTE = models.FloatField(default = 0)
	proposed_total_FTE = models.FloatField(default = 0)

	present_total_salary = models.FloatField(default = 0)
	proposed_total_salary = models.FloatField(default = 0)



	department_percentile = models.FloatField(blank = True, null = True)
	position_percentile = models.FloatField(blank = True, null = True)
	college_percentile = models.FloatField(blank = True, null = True)
	total_percentile = models.FloatField(blank = True, null = True)

	# python manage.py shell
	# import...
	# for e in Employee.objects.all():
	#	e.save()
	####This takes for fucking ever. Go get coffee. Take a shower. Run a few miles. Take another shower.####
	
	def save_stats(self):
		print "getting department rank"
		self.department_percentile = self.get_department_percentile()
		print "getting position rank"
		self.position_percentile = self.get_position_percentile()
		print "getting college rank"
		self.college_percentile = self.get_college_percentile()
		print "getting total rank"
		self.total_percentile = self.get_total_percentile()


	def save(self, **kwargs):
		self.save_stats()
		super(self.__class__, self).save(**kwargs)

	def get_primary_employment(self):
		employeedetails = EmployeeDetail.objects.filter(identity = self)
		
		k = employeedetails[0]

		for employee in employeedetails:
			if employee.proposed_salary > k.proposed_salary:
				k = employee
		return k

	def get_position_percentile(self):
		all_salaries = []

		primary_employment = self.get_primary_employment()
		members = EmployeeDetail.objects.filter(position = primary_employment.position)

		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		my_salary = self.proposed_total_salary
		print my_salary
		print all_salaries
		percentile_thing = stats.percentileofscore(all_salaries, my_salary, kind='strict')
		print percentile_thing
		return percentile_thing

	def get_department_percentile(self):
		all_salaries = []

		primary_employment = self.get_primary_employment()
		department_members = EmployeeDetail.objects.filter(department = primary_employment.department)

		for member in department_members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		my_salary = self.proposed_total_salary
		print my_salary
		print all_salaries
		percentile_thing = stats.percentileofscore(all_salaries, my_salary, kind='strict')
		print percentile_thing
		return percentile_thing

	def get_college_percentile(self):
		all_salaries = []

		primary_employment = self.get_primary_employment()
		members = EmployeeDetail.objects.filter(college = primary_employment.college)

		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		my_salary = self.proposed_total_salary
		print my_salary
		print all_salaries
		percentile_thing = stats.percentileofscore(all_salaries, my_salary, kind='strict')
		print percentile_thing
		return percentile_thing

	def get_total_percentile(self):
		all_salaries = []

		members = Employee.objects.all()

		for member in members:
			if member.proposed_total_salary > 0:
				all_salaries.append(int(member.proposed_total_salary))

		my_salary = self.proposed_total_salary
		
		percentile_thing = stats.percentileofscore(all_salaries, my_salary, kind='strict')
		print percentile_thing
		return percentile_thing


	#write a def to find their primary employment. Test of FTE and Salary majority.


	#this is a simple start. what else do I need?
	#Lots of interesting things that will come up with professors. 
	#chaired?	
	#get a list of questions that we need answered. Find the fields we'll need to create in order to do so.
	
	def __unicode__(self):
		return self.identity.name

class EmployeeDetail(models.Model):
	identity = models.ForeignKey(Employee)
	position = models.ForeignKey(Position)
	
	college = models.ForeignKey(College)
	department = models.ForeignKey(Department)
	organization = models.ForeignKey(Organization)

	tenure = models.CharField(max_length = 5, blank = True)
	present_FTE = models.FloatField(default = 0)
	proposed_FTE = models.FloatField(default = 0)

	present_salary = models.FloatField(default = 0)
	proposed_salary = models.FloatField(default = 0)

	def __unicode__(self):
		return self.identity.identity.name
		
	class Meta:
		ordering = ['-proposed_salary']