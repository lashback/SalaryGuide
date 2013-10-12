from django.contrib import admin

from apps.salaries.models import *


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['identity','proposed_total_salary','year']

class EmployeeDetailAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'position', 'college', 'proposed_salary']
	search_fields = ['identity__name']


class CollegeAdmin(admin.ModelAdmin):
	list_display=['name', 'campus', 'total_budget']
	list_filter = ('campus',)


class DepartmentAdmin(admin.ModelAdmin):
	list_display=['name', 'college', 'total_budget']
	list_filter = ('college', 'college__campus')

class PositionAdmin(admin.ModelAdmin):
	list_display = ['title']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(EmployeeDetail, EmployeeDetailAdmin)
admin.site.register(Position, PositionAdmin)

