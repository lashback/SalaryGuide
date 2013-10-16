from django.db import models
#from django import forms #i don't actually know what this does and I don't ahve internet so just going with it.
#from numpy import percentile
from nameparser import HumanName
from scipy import stats

import numpy

import math
import functools


class Institution(models.Model):
#this is the university. allows for inclusion of other schools if you're interested.
	name = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.name

class Campus(models.Model):
	name = models.CharField(max_length = 50)
	institution = models.ForeignKey(Institution)
	def __unicode__(self):
		return self.name

class College(models.Model):
	name = models.CharField(max_length = 50)
	campus = models.ForeignKey(Campus)
	campus_salary_average_percentile = models.FloatField(null = True, blank = True)
	median_salary = models.FloatField(null = True, blank=True)
	average_salary = models.FloatField(null=True, blank = True)
	max_salary = models.FloatField(null=True, blank = True)
	full_time_employees = models.FloatField(null = True, blank = True)
	individual_employees = models.IntegerField(null = True, blank = True)
	salaries_sum = models.IntegerField(null=True, blank = True)



	#code = models.CharField(max_length = 5)

	total_budget = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
		#self.median_salary = self.get_median_salary()
		self.salaries_sum = self.get_sum()
		super(College, self).save(*args, **kwargs)

	def get_median_salary(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = []
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))
		median = numpy.median(all_salaries)
		print median
		print self.name
		return median
	def get_max_salary(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = []
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		maximum = numpy.maximum(all_salaries)
		return maximum

	def get_full_time(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = []
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		maximum = numpy.sum(all_hours)
		return maximum


	def get_keyed_salaries(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = {}
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries[member.identity.id] = []
				all_salaries[member.identity.id].append(int(member.identity.proposed_total_salary))
		return all_salaries

	def get_salaries(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = []
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))
		return all_salaries

	def get_sum(self):
		members = EmployeeDetail.objects.filter(college = self)
		college_salaries = []
		for member in members:
			college_salaries.append(int(member.proposed_salary))

		sum = numpy.sum(college_salaries)
		return sum



class Department(models.Model):
	name = models.CharField(max_length=50)
	college = models.ForeignKey(College)
	total_budget = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)

	def get_salaries(self):
		members = EmployeeDetail.objects.filter(college = self)
		all_salaries = {}
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries[member.identity.name]
				all_salaries.append(int(member.identity.proposed_total_salary))
		return all_salaries

class Organization(models.Model):
	name = models.CharField(max_length=255)
	department = models.ForeignKey(Department)
	total_budget = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)

class Position(models.Model):
	title = models.CharField(max_length = 50)
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
	name = models.CharField(max_length = 50)
	full_name = models.CharField(max_length = 50, null = True)
	first_name = models.CharField(max_length=30, null = True)
	last_name = models.CharField(max_length=35, null = True)
	middle = models.CharField(max_length=30, null = True)
#	mug = models.ForeignKey(Mug, null = True, blank = True)
	
	def save(self, *args, **kwargs):
		parsed_name = HumanName(self.name)
		print parsed_name
		self.full_name = parsed_name
		self.first_name = parsed_name.first
		print self.first_name
		self.last_name = parsed_name.last
		self.middle = parsed_name.middle

		super(EmployeeSuper, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s %s" % (self.first_name, self.middle, self.last_name, )

class Mug(models.Model):
	identity = models.ForeignKey(EmployeeSuper, null = True)
	image = models.ImageField(upload_to = 'img/mugs')
	def __unicode__(self):
		return "Mug for %s" %(self.identity)
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
	department_position_percentile = models.FloatField(blank = True, null = True)
	college_position_percentile = models.FloatField(blank = True, null = True)


	# python manage.py shell
	# import...
	# for e in Employee.objects.all():
	#	e.save()
	####This takes for fucking ever. Go get coffee. Take a shower. Run a few miles. Take another shower.####
	
#	def save_stats(self):
#		print "getting department rank"
#		self.department_percentile = self.get_department_percentile()
#		print "getting position rank"
#		self.position_percentile = self.get_position_percentile()
#		print "getting college rank"
#		self.college_percentile = self.get_college_percentile()
#		print "getting total rank"
#		self.total_percentile = self.get_total_percentile()


	def save(self, **kwargs):
		#print "getting department rank"
		#self.department_percentile = self.get_department_percentile()
		#print self.identity.name
		#print "getting position rank"
		#self.position_percentile = self.get_position_percentile()
		#print "getting college rank"
		#self.college_percentile = self.get_college_percentile()
		#print "getting total rank"
		#self.total_percentile = self.get_total_pecentile()
	#	primary_empl = self.get_primary_employment()
	#	thang = None
	#	self.college_position_percentile = self.get_rank_according_to_things(primary_empl.college, thang, primary_empl.position)
	#	thing = None
	#	self.department_position_percentile = self.get_rank_according_to_things(thing, primary_empl.department, primary_empl.position)

		super(self.__class__, self).save(**kwargs)



	def get_rank_according_to_things(self, college = None, department = None, position = None):
		kwargs = {}
		if college:
			kwargs['college'] = college
		if department:
			kwargs['department'] = department
		if position:
			kwargs['position'] = position

		members = EmployeeDetail.objects.filter(**kwargs)

		all_salaries = []
		for member in members:
			if member.identity.proposed_total_salary > 0:
				all_salaries.append(int(member.identity.proposed_total_salary))

		self_salary = self.proposed_total_salary
		rank = stats.percentileofscore(all_salaries, self_salary, kind='strict')
		print self.id
		print rank

		return rank



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
		return "%s %s (%s)" % (self.identity.first_name, self.identity.last_name, self.identity.middle,)

class EmployeeDetail(models.Model):
	identity = models.ForeignKey(Employee)
	position = models.ForeignKey(Position)
	
	college = models.ForeignKey(College)
	department = models.ForeignKey(Department)

	employee_class = models.CharField(max_length = 5, null = True, blank = True)
	tenure = models.CharField(max_length = 5, blank = True)
	present_FTE = models.FloatField(default = 0)
	proposed_FTE = models.FloatField(default = 0)

	present_salary = models.FloatField(default = 0)
	proposed_salary = models.FloatField(default = 0)

	def __unicode__(self):
		return self.identity.identity.name
		
	class Meta:
		ordering = ['-proposed_salary']

