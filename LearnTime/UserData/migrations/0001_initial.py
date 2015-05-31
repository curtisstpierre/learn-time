# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_absence', models.DateTimeField(verbose_name=b'Date Absent')),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField(verbose_name=b'Start Date')),
                ('endDate', models.DateField(verbose_name=b'End Date')),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('daysOfWeek', models.CharField(default=b'MON', max_length=3, choices=[(b'MON', b'Monday'), (b'TUE', b'Tuesday'), (b'WED', b'Wednesday'), (b'THU', b'Thursday'), (b'FRI', b'Friday'), (b'SAT', b'Saturday'), (b'SUN', b'Sunday')])),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
                ('course', models.ForeignKey(to='userdata.Course')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=200, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.CreateModel(
            name='Simple_Payee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('CPF', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
                ('course', models.ForeignKey(to='userdata.Offering')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('number', models.IntegerField(max_length=200)),
                ('compliment', models.CharField(max_length=200, blank=True)),
                ('neighborhood', models.CharField(max_length=200)),
                ('CEP', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('RG', models.IntegerField(max_length=200)),
                ('CPF', models.IntegerField(max_length=200)),
                ('DOB', models.DateField(verbose_name=b'Data Nasc.')),
                ('telephone', models.TextField(max_length=200)),
                ('mothersName', models.CharField(max_length=200)),
                ('fathersName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
                ('payee', models.ForeignKey(blank=True, to='userdata.StudentData', null=True)),
                ('simple_payee', models.ForeignKey(blank=True, to='userdata.Simple_Payee', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
            ],
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(to='userdata.StudentData'),
        ),
        migrations.AddField(
            model_name='reportcard',
            name='course',
            field=models.ForeignKey(to='userdata.StudentCourse'),
        ),
        migrations.AddField(
            model_name='offering',
            name='students',
            field=models.ManyToManyField(to='userdata.StudentData', through='userdata.StudentCourse'),
        ),
        migrations.AddField(
            model_name='offering',
            name='teacher',
            field=models.ForeignKey(to='userdata.Teacher'),
        ),
        migrations.AddField(
            model_name='homework',
            name='course',
            field=models.ForeignKey(to='userdata.StudentCourse'),
        ),
        migrations.AddField(
            model_name='absence',
            name='course',
            field=models.ForeignKey(to='userdata.StudentCourse'),
        ),
    ]
