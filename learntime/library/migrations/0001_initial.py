# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('Type', models.CharField(default=b'COM', max_length=3, choices=[(b'NOV', b'Novel'), (b'COM', b'Comic Book'), (b'MAG', b'Magazine')])),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_taken', models.DateField(blank=True)),
                ('duration', models.IntegerField(max_length=2)),
                ('date_returned', models.DateField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Entered')),
                ('course', models.ForeignKey(to='library.Book')),
                ('student', models.ForeignKey(to='userdata.StudentData')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='students',
            field=models.ManyToManyField(to='userdata.StudentData', through='library.Borrow'),
        ),
    ]
