from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=500, null=False)
    slug = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)
    active = models.BooleanField(default=False)
    thumbnail = models.CharField(max_length=2500, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

