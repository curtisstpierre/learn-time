from django.db import models
from userdata.models import StudentData


class Book(models.Model):
    name = models.CharField(max_length=200)
    NOVEL = 'NOV'
    COMICBOOK = 'COM'
    MAGAZINE = 'MAG'
    TYPE = (
        (NOVEL, 'Novel'),
        (COMICBOOK, 'Comic Book'),
        (MAGAZINE, 'Magazine'),
    )
    Type = models.CharField(max_length=3,
                            choices=TYPE,
                            default=COMICBOOK)
    students = models.ManyToManyField(StudentData, through='Borrow')


class Borrow(models.Model):
    student = models.ForeignKey(StudentData)
    course = models.ForeignKey(Book)
    date_taken = models.DateField(blank=True)
    duration = models.IntegerField(max_length=2)
    date_returned = models.DateField(blank=True)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name
