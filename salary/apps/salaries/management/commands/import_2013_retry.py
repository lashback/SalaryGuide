import csv
import os
import re
import glob
from string import split
from django.core.management.base import BaseCommand

from apps.salaries.models import *
from settings.common import SITE_ROOT


class Command(BaseCommand):
	def handle(self, *args, **options):
		working_dir = os.path.join(SITE_ROOT, '../data/2013/salaries/')

		#file_path = os.path.join(working_dir, 'Urbana-GB.csv')

		csv_list = glob.glob(working_dir + "*-GB.csv")
		for sheet in csv_list:

			handle = csv.reader(open(sheet, 'rU'), delimiter=',', quotechar='"')
			handle.next()


			for index, h in enumerate(handle):
				try:
				#print index
				#print '\n'.join(h)

					university_import, university_created = Institution.objects.get_or_create(
						name = 'University of Illinois'
						)
					#print university_import.name
					campus_import, campus_created = Campus.objects.get_or_create(
						institution = university_import, 
						name = h[17].strip()
						)
					#print campus_import.name
					college_import, college_created = College.objects.get_or_create(
						name = h[1].strip(),
						campus = campus_import
						)
					#print college_import.name
					department_import, department_created = Department.objects.get_or_create(
						name = h[3].strip(),
						college = college_import
						)
					#print department_import.name
					position_import, position_created = Position.objects.get_or_create(
						title = h[5].strip(),
						)
					#print position_import.title
					super_employee_import, employee_super_created = EmployeeSuper.objects.get_or_create(
						name = h[4].strip()
						)

					#print super_employee_import.name
					year = 2013
					
					employee_import, employee_created = Employee.objects.get_or_create(
						year = year,
						identity = super_employee_import,
						present_total_FTE = h[12].strip(),
						proposed_total_FTE = h[13].strip(),
						present_total_salary = h[14].strip(),
						proposed_total_salary = h[15].strip(),
					)
					#print employee_created
					#print "did i do it?"
					detail_import, detail_created = EmployeeDetail.objects.get_or_create(
						identity = employee_import,
						position = position_import,
						college = college_import,
						department = department_import,
						
						tenure = h[6].strip(),
						employee_class = h[7].strip(),
						present_FTE = h[8].strip(),
						proposed_FTE = h[9].strip(),

						present_salary = h[10].strip(),
						proposed_salary = h[11].strip()
						)
					#print 'we didit'

				except IndexError:
					print "Fuck index errors"
					