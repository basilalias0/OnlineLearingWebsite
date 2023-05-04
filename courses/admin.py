from django.contrib import admin
from courses.models import Course, Teacher
from courses.models import Video
from courses.models import UserCourse
from courses.models import Payment


class TeacherAdmin(admin.TabularInline):
    model = Teacher


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TeacherAdmin, VideoAdmin]
    list_display = ['name', 'price', 'active']
    list_filter = ['active']

class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['order_id', 'user', 'course', 'status']
    list_filter = ["course", 'status']


admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Teacher)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(UserCourse)





