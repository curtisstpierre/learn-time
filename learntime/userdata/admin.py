from django.contrib import admin
from userdata.models import StudentData, Offering, \
    StudentCourse, Course, Teacher


class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentCourseInline,)


class OfferingAdmin(admin.ModelAdmin):
    inlines = (StudentCourseInline,)

admin.site.register(StudentData, StudentAdmin)
admin.site.register(Offering, OfferingAdmin)
admin.site.register(Course)
admin.site.register(Teacher)
