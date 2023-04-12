from django.shortcuts import render
from courses.models import Course
from courses.models import Video
from django.shortcuts import redirect


def video(request, slug):
    print(request.user)
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('Lecture')
    vid = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    videos = Video.objects.get(serial_number=serial_number, course=course)
    print(videos.is_preview)
    if ((request.user.is_authenticated is False) and (videos.is_preview is False)):
        return redirect("login")
    context = {
        "course": course,
        "videos": videos,
        "vid": vid
        }
    return render(request, template_name="courses/video.html",
                  context=context)

