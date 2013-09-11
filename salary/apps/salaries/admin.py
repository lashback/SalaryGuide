from django.contrib import admin

from apps.salaries.models import *


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['identity','proposed_total_salary']

class EmployeeDetailAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'position', 'college', 'organization', 'proposed_salary']

class CollegeAdmin(admin.ModelAdmin):
	list_display=['name', 'campus', 'total_budget']
	list_filter = ('campus',)


class DepartmentAdmin(admin.ModelAdmin):
	list_display=['name', 'college', 'total_budget']
	list_filter = ('college',)

class OrganizationAdmin(admin.ModelAdmin):
	list_display = ['name','department', 'total_budget']
	list_filter = ('department',)

class PositionAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(EmployeeDetail, EmployeeDetailAdmin)
