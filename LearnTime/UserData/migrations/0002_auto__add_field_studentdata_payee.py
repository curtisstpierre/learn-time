# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StudentData.payee'
        db.add_column(u'UserData_studentdata', 'payee',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserData.StudentData'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StudentData.payee'
        db.delete_column(u'UserData_studentdata', 'payee_id')


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
            'payee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UserData.StudentData']", 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'telephone': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['UserData']