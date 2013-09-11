from django.http import HttpResponse
from django.template import Context, loader
from apps.salaries.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Sum, Avg, Max, Min, StdDev, Variance
from django.template import RequestContext

def employee(request, employee_id):
	p = get_object_or_404(Employee, pk = employee_id)
	return render_to_response('employee.html', {'employee':p})

def college(college, college_id):
	p = get_object_or_404(College, pk = college_id)
	employees = p.employee_set.all
	
	return render_to_response('college.html', {'employees':employees, 'college':p})

