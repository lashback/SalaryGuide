# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Employee.department_percentile'
        db.add_column(u'salaries_employee', 'department_percentile',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Employee.department_percentile'
        db.delete_column(u'salaries_employee', 'department_percentile')


    models = {
        u'salaries.campus': {
            'Meta': {'object_name': 'Campus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Institution']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'salaries.college': {
            'Meta': {'object_name': 'College'},
            'campus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Campus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_budget': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'salaries.department': {
            'Meta': {'object_name': 'Department'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.College']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_budget': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'salaries.employee': {
            'Meta': {'object_name': 'Employee'},
            'department_percentile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.EmployeeSuper']"}),
            'present_total_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'present_total_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_total_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_total_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'salaries.employeedetail': {
            'Meta': {'ordering': "['-proposed_salary']", 'object_name': 'EmployeeDetail'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.College']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Employee']"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Organization']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Position']"}),
            'present_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'present_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tenure': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'salaries.employeesuper': {
            'Meta': {'object_name': 'EmployeeSuper'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'salaries.institution': {
            'Meta': {'object_name': 'Institution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'salaries.organization': {
            'Meta': {'object_name': 'Organization'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_budget': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'salaries.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['salaries']