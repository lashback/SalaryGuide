import csv
import os
import re

from string import split
from django.core.management.base import BaseCommand

from apps.salaries.models import *
from settings.common import SITE_ROOT

class Command(BaseCommand):
	def handle(self, *args, **options):
		working_dir = os.path.join(SITE_ROOT, '../data')
		file_path = os.path.join(working_dir, '2012GreyBook.csv')

		handle = csv.reader(open(file_path, 'rU'), delimiter=',', quotechar='"')
		handle.next()

		for index, h in enumerate(handle):
			university_import, university_created = Institution.objects.get_or_create(
				name = 'University of Illinois'
				)

			campus_import, campus_created = Campus.objects.get_or_create(
				institution = university_import, 
				name = h[15].strip()
				)

			college_import, college_created = College.objects.get_or_create(
				name = h[0].strip(),
				campus = campus_import
				)

			department_import, department_created = Department.objects.get_or_create(
				name = h[2].strip(),
				college = college_import
				)

			organization_import, organization_created = Organization.objects.get_or_create(
				name = h[3].strip(),
				department = department_import
				)

			position_import, position_created = Position.objects.get_or_create(
				title = h[5].strip(),
				)

			super_employee_import, employee_super_created = EmployeeSuper.objects.get_or_create(
				name = h[4].strip()
				)

			employee_import, employee_created = Employee.objects.get_or_create(
				identity = super_employee_import,
				year = 2012,
				present_total_FTE = h[11].strip(),
				proposed_total_FTE = h[12].strip(),
				present_total_salary = h[13].strip(),
				proposed_total_salary = h[14].strip()
				)
			detail_import, detail_created = EmployeeDetail.objects.get_or_create(
				identity = employee_import,
				position = position_import,
				college = college_import,
				department = department_import,
				organization = organization_import,

				tenure = h[6].strip(),

				present_FTE = h[7].strip(),
				proposed_FTE = h[8].strip(),

				present_salary = h[9].strip(),
				proposed_salary = h[10].strip()

				)