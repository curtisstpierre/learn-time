# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table(u'UserData_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['Teacher'])

        # Adding model 'StudentCourse'
        db.create_table(u'UserData_studentcourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.StudentData'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.Offering'])),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['StudentCourse'])

        # Adding model 'Offering'
        db.create_table(u'UserData_offering', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.Teacher'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.Course'])),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('startTime', self.gf('django.db.models.fields.TimeField')()),
            ('endTime', self.gf('django.db.models.fields.TimeField')()),
            ('daysOfWeek', self.gf('django.db.models.fields.CharField')(default='MON', max_length=3)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['Offering'])

        # Adding model 'Course'
        db.create_table(u'UserData_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['Course'])


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table(u'UserData_teacher')

        # Deleting model 'StudentCourse'
        db.delete_table(u'UserData_studentcourse')

        # Deleting model 'Offering'
        db.delete_table(u'UserData_offering')

        # Deleting model 'Course'
        db.delete_table(u'UserData_course')


    models = {
        u'UserData.course': {
            'Meta': {'object_name': 'Course'},
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
        u'UserData.studentcourse': {
            'Meta': {'object_name': 'StudentCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.Offering']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentData']"})
        },
        u'UserData.studentdata': {
            'CEP': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'DOB': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'StudentData'},
            'RG': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'compliment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'fathersName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mothersName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'payee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentData']", 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
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