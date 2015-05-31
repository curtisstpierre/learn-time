from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name


class Simple_Payee(models.Model):
    name = models.CharField(max_length=200)
    CPF = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.IntegerField(max_length=200)
    compliment = models.CharField(max_length=200, blank=True)
    neighborhood = models.CharField(max_length=200)
    CEP = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    RG = models.IntegerField(max_length=200)
    CPF = models.IntegerField(max_length=200)
    DOB = models.DateField('Data Nasc.')
    telephone = models.TextField(max_length=200)
    mothersName = models.CharField(max_length=200)
    fathersName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pub_date = models.DateTimeField('Date Entered')
    payee = models.ForeignKey('self', null=True, blank=True)
    simple_payee = models.ForeignKey(Simple_Payee, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name


class Offering(models.Model):
    teacher = models.ForeignKey(Teacher)
    course = models.ForeignKey(Course)
    startDate = models.DateField('Start Date')
    endDate = models.DateField('End Date')
    startTime = models.TimeField()
    endTime = models.TimeField()
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    DAY_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    daysOfWeek = models.CharField(max_length=3,
                                  choices=DAY_OF_WEEK,
                                  default=MONDAY)
    #students = models.ManyToManyField #list of students
    students = models.ManyToManyField(StudentData, through='StudentCourse')
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return str(self.course) + ': ' + str(self.teacher)


class StudentCourse(models.Model):
    student = models.ForeignKey(StudentData)
    course = models.ForeignKey(Offering)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return str(self.student) + ': ' + str(self.course)


class ReportCard(models.Model):
    course = models.ForeignKey(StudentCourse)
    grade = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name


class Absence(models.Model):
    course = models.ForeignKey(StudentCourse)
    date_of_absence = models.DateTimeField('Date Absent')
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name


class homework(models.Model):
    course = models.ForeignKey(StudentCourse)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Entered')

    def __unicode__(self):
        return self.name
