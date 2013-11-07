from django.contrib import admin

from apps.salaries.models import *


class EmployeeAdmin(admin.ModelAdmin):
	search_fields = ['identity__name']
	list_display = ['identity','proposed_total_salary','year']

class EmployeeDetailAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'position', 'college', 'proposed_salary']
	search_fields = ['identity__identity__name']
	list_filter = ('is_primary', 'identity__year', 'is_non_GB')


class CollegeAdmin(admin.ModelAdmin):
	list_display=['name', 'campus', 'total_budget']
	list_filter = ('campus',)

class EmployeeClassAdmin(admin.ModelAdmin):
	list_display = ['acronym', 'description']
	list_filter = ('description',)

class DepartmentAdmin(admin.ModelAdmin):
	list_display=['name', 'college', 'total_budget']
	list_filter = ('college', 'college__campus')

class PositionAdmin(admin.ModelAdmin):
	list_display = ['title']

class EmployeeSuperAdmin(admin.ModelAdmin):
	search_fields = ['name', 'first_name']
	list_display = ['name', 'first_name', 'last_name', 'middle']

class MugAdmin(admin.ModelAdmin):
	raw_id_fields = ('identity',)
	

admin.site.register(Mug, MugAdmin)
admin.site.register(EmployeeClass, EmployeeClassAdmin)
admin.site.register(EmployeeSuper, EmployeeSuperAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(EmployeeDetail, EmployeeDetailAdmin)
admin.site.register(Position, PositionAdmin)

