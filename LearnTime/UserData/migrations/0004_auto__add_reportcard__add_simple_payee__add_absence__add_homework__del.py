# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReportCard'
        db.create_table(u'UserData_reportcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.StudentCourse'])),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['ReportCard'])

        # Adding model 'Simple_Payee'
        db.create_table(u'UserData_simple_payee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('CPF', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['Simple_Payee'])

        # Adding model 'Absence'
        db.create_table(u'UserData_absence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.StudentCourse'])),
            ('date_of_absence', self.gf('django.db.models.fields.DateTimeField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['Absence'])

        # Adding model 'homework'
        db.create_table(u'UserData_homework', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.StudentCourse'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['homework'])

        # Deleting field 'StudentCourse.grade'
        db.delete_column(u'UserData_studentcourse', 'grade')

        # Adding field 'StudentData.CPF'
        db.add_column(u'UserData_studentdata', 'CPF',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=200),
                      keep_default=False)

        # Adding field 'StudentData.simple_payee'
        db.add_column(u'UserData_studentdata', 'simple_payee',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.Simple_Payee'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ReportCard'
        db.delete_table(u'UserData_reportcard')

        # Deleting model 'Simple_Payee'
        db.delete_table(u'UserData_simple_payee')

        # Deleting model 'Absence'
        db.delete_table(u'UserData_absence')

        # Deleting model 'homework'
        db.delete_table(u'UserData_homework')

        # Adding field 'StudentCourse.grade'
        db.add_column(u'UserData_studentcourse', 'grade',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)

        # Deleting field 'StudentData.CPF'
        db.delete_column(u'UserData_studentdata', 'CPF')

        # Deleting field 'StudentData.simple_payee'
        db.delete_column(u'UserData_studentdata', 'simple_payee_id')


    models = {
        u'UserData.absence': {
            'Meta': {'object_name': 'Absence'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentCourse']"}),
            'date_of_absence': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'UserData.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'UserData.homework': {
            'Meta': {'object_name': 'homework'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentCourse']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'UserData.offering': {
            'Meta': {'object_name': 'Offering'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.Course']"}),
            'daysOfWeek': ('django.db.models.fields.CharField', [], {'default': "'MON'", 'max_length': '3'}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'endTime': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'startTime': ('django.db.models.fields.TimeField', [], {}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['UserData.StudentData']", 'through': u"orm['UserData.StudentCourse']", 'symmetrical': 'False'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.Teacher']"})
        },
        u'UserData.reportcard': {
            'Meta': {'object_name': 'ReportCard'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentCourse']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'UserData.simple_payee': {
            'CPF': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Simple_Payee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'UserData.studentcourse': {
            'Meta': {'object_name': 'StudentCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.Offering']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentData']"})
        },
        u'UserData.studentdata': {
            'CEP': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'CPF': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'DOB': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'StudentData'},
            'RG': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'compliment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'fathersName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mothersName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'payee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentData']", 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'simple_payee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.Simple_Payee']", 'null': 'True'}),
            'telephone': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'UserData.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['UserData']