from django.http import HttpResponse
from django.template import Context, loader
from apps.salaries.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
import os
from django.template import RequestContext
#this isn't working
from django.core.context_processors import csrf

import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet


import numpy

def landing(request):
	campuses = Campus.objects.all()
	return render_to_response('landing.html', {'campuses':campuses})

def campus(request, campus_id):
	p = get_object_or_404(Campus, pk = campus_id)
	colleges = College.objects.filter(campus = p)
	chancellor = EmployeeDetail.objects.filter(position__title = 'CHANCELLOR')
	return render_to_response('campus.html', {'campus':p, 'colleges':colleges, 'chancellor':chancellor})

def employeeSuper(request, employeeSuper_id):
	p = get_object_or_404(EmployeeSuper, pk = employeeSuper_id)
	
	primary = p.get_primary_employment()

	#####this hits the database. We don't want to do that. #####
	college_employees = EmployeeDetail.objects.filter(college=primary.college, identity__year = 2013, is_primary = True) 
	#college_employees = EmployeeDetail.objects.filter(college__campus=primary.college.campus, identity__year = 2013, is_primary = True) 
	college_salaries = []
	for e in college_employees:
		college_salaries.append(e.identity.proposed_total_salary)
	
	######this pulls stuff from a static folder but I don't like it.

	#college_salaries = []
	#source = open(os.path.join(settings.STATIC_ROOT, 'json', '%s.json' % (primary.college.name,)))
	#for line in source.readlines():
	#		college_salaries.append(line)

	return render_to_response('employeeSuper.html', {'employee':p, 'primary':primary, 'college_salaries':college_salaries})

def college(request, college_id):
	p = get_object_or_404(College, pk = college_id)
	
	employees = p.employeedetail_set.all

	deans = EmployeeDetail.objects.filter(college = p, position__title = 'DEAN')

	
	return render_to_response('college.html', {'employees':employees, 'college':p, 'deans':deans})

def department(request, department_id):
	p = get_object_or_404(Department, pk = department_id)
	employees = p.employeedetail_set.all
	heads = EmployeeDetail.objects.filter(department = p, position__title__contains = 'HEAD')

	return render_to_response('department.html', {'employees':employees, 'department':p, 'heads':heads})

def position(request, position_id):
	p = get_object_or_404(Position, pk = position_id)
	employees = p.employeedetail_set.all

	return render_to_response('position.html', {'employees':employees, 'position':p})

def bubbles(request):
	colleges = College.objects.all()
	return render_to_response('bubbles.html', {'colleges':colleges})


def autocomplete(request):
	sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:10]
	##### Return these fuckers with keys #####
	#suggestions = []

	data = []

	for result in sqs:
		
		#so get the full set, but there should only be one attribute.
		primary = result.object.get_primary_employment()


		data.append({
			'name': str(result.full_name), 
			'id': result.object.id,
			'position': primary.position.title,
			'campus': primary.college.campus.name
			}
			)


	full_response =  json.dumps(data) 

#    	suggestions.append([{'name': str(result.full_name), 'id':result.object.id},])
    
 #   the_data = suggestions
##### Don't know. #####
	#suggestions = [result.full_name for result in sqs]
	#suggestion_ids = [result.object.id for result in sqs]
	#data = json.dumps({
	#	'results': suggestions,
		#'ids':suggestion_ids

	#})
	
	return HttpResponse(full_response, content_type='application/json')

def deans(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="employee_equity.csv"'

	# The data is hard-coded here, but you could load it from a database or
	# some other source.
	csv_data = [('Name', 'Primary Position', 'Campus', 'College', 'Department', 'College Faculty Median Salary', 'Department Median Faculty Salary', 'Employee total salary', 'Difference from College Faculty Median', 'Difference from Department Faculty Median')]
	for dean in EmployeeDetail.objects.filter(identity__year = 2013, is_primary = True):
		dept_difference = dean.identity.proposed_total_salary - dean.department.median_faculty_salary
		college_difference = dean.identity.proposed_total_salary - dean.college.median_faculty_salary

		csv_data += (
				 (dean.identity.identity.name, dean.position.title, dean.college.campus.name, dean.college.name, dean.department.name, dean.college.median_faculty_salary, dean.department.median_faculty_salary, dean.identity.proposed_total_salary, college_difference, dept_difference),
		)

	t = loader.get_template('deans.txt')
	c = Context({
	    'data': csv_data,
	})
	response.write(t.render(c))
	return response