from django.shortcuts import render
from courses.models import Course


def courses(request):
    course = Course.objects.all()
    context = {
        "course": course
        }
    return render(request, template_name="courses/courses.html",
                  context=context)
