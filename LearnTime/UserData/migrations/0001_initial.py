# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudentData'
        db.create_table(u'UserData_studentdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('compliment', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('CEP', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('RG', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('DOB', self.gf('django.db.models.fields.DateTimeField')()),
            ('telephone', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('mothersName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fathersName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'UserData', ['StudentData'])


    def backwards(self, orm):
        # Deleting model 'StudentData'
        db.delete_table(u'UserData_studentdata')


    models = {
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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'telephone': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['UserData']