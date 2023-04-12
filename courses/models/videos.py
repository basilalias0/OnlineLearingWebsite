from django.db import models
from courses.models import Course


class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    serial_number = models.IntegerField(null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    id = models.CharField(max_length=2500, null=False,primary_key=True)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title

