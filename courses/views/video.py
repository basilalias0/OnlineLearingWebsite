from django.shortcuts import render
from courses.models import Course,UserCourse
from courses.models import Video
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def mycourses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user = user)
    context={
        "user_courses" : user_courses
    }
    return render(request = request, template_name="courses/my_courses.html", context=context)
def video(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('Lecture')
    vid = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    videos = Video.objects.get(serial_number=serial_number, course=course)
    if videos.is_preview is False:
        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect("checkout", slug=course.slug)

    context = {
        "course": course,
        "videos": videos,
        "vid": vid
        }
    return render(request, template_name="courses/video.html",
                  context=context)

