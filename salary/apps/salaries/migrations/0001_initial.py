# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institution'
        db.create_table(u'salaries_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'salaries', ['Institution'])

        # Adding model 'Campus'
        db.create_table(u'salaries_campus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Institution'])),
        ))
        db.send_create_signal(u'salaries', ['Campus'])

        # Adding model 'College'
        db.create_table(u'salaries_college', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('campus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Campus'])),
            ('total_budget', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'salaries', ['College'])

        # Adding model 'Department'
        db.create_table(u'salaries_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.College'])),
            ('total_budget', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'salaries', ['Department'])

        # Adding model 'Organization'
        db.create_table(u'salaries_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Department'])),
            ('total_budget', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'salaries', ['Organization'])

        # Adding model 'Position'
        db.create_table(u'salaries_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'salaries', ['Position'])

        # Adding model 'EmployeeSuper'
        db.create_table(u'salaries_employeesuper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'salaries', ['EmployeeSuper'])

        # Adding model 'Employee'
        db.create_table(u'salaries_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.EmployeeSuper'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('present_total_FTE', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('proposed_total_FTE', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('present_total_salary', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('proposed_total_salary', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('department_percentile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('position_percentile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('college_percentile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_percentile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'salaries', ['Employee'])

        # Adding model 'EmployeeDetail'
        db.create_table(u'salaries_employeedetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Employee'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Position'])),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.College'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Department'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Organization'])),
            ('tenure', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('present_FTE', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('proposed_FTE', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('present_salary', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('proposed_salary', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'salaries', ['EmployeeDetail'])


    def backwards(self, orm):
        # Deleting model 'Institution'
        db.delete_table(u'salaries_institution')

        # Deleting model 'Campus'
        db.delete_table(u'salaries_campus')

        # Deleting model 'College'
        db.delete_table(u'salaries_college')

        # Deleting model 'Department'
        db.delete_table(u'salaries_department')

        # Deleting model 'Organization'
        db.delete_table(u'salaries_organization')

        # Deleting model 'Position'
        db.delete_table(u'salaries_position')

        # Deleting model 'EmployeeSuper'
        db.delete_table(u'salaries_employeesuper')

        # Deleting model 'Employee'
        db.delete_table(u'salaries_employee')

        # Deleting model 'EmployeeDetail'
        db.delete_table(u'salaries_employeedetail')


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
            'college_percentile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'department_percentile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salaries.EmployeeSuper']"}),
            'position_percentile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'present_total_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'present_total_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_total_FTE': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'proposed_total_salary': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total_percentile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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