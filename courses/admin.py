from django.contrib import admin
from courses.models import Course, Teacher
from courses.models import Video


class TeacherAdmin(admin.TabularInline):
    model = Teacher


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TeacherAdmin, VideoAdmin]


admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Teacher)





