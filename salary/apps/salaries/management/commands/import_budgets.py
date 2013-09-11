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
		file_path = os.path.join(working_dir, 'dmi_budget.csv')

		handle = csv.reader(open(file_path, 'rU'), delimiter = ',',quotechar='"')
		handle.next()

		for index, h in enumerate(handle):
			
			if h[3].strip() == '2000':
				print h[2].strip()
				code = h[1].strip()
				budget = h[5].strip()
				print budget
				try: 
					#budget = budget * 1000
					if code[-7:] == 'XXX-XXX':
						for c in College.objects.filter(total_budget=0):
							if c.name == h[2].strip():

								c.total_budget = budget
								print '%s saved with budget of' % (c.name,)
								print c.total_budget
								c.save()

					else:
							for d in Department.objects.filter(total_budget = 0):
								if d.name == h[2].strip():
									d.total_budget = budget
									d.save()

							for o in Organization.objects.filter(total_budget = 0):
								if o.name == h[2].strip():
									o.total_budget = budget
									o.save()
				except (RuntimeError, ValueError, AttributeError, TypeError, NameError):
					print 'Errrroorrr'
					
