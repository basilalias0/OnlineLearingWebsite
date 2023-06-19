from django.shortcuts import render
from courses.models import Course
from django.shortcuts import redirect
from Prodigyy.settings import KEY_ID, KEY_SECRET
from courses.models.payment import Payment, UserCourse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = None

    if not request.user.is_authenticated :
        return redirect("login")
    user = request.user
    action = request.GET.get('action')
    order = None
    error = None
    payment = None
    if action == 'create_payment':

        try:
            user_course = UserCourse.objects.get(user = user, course = course)
            error = "You Already Enrolled In This Course!!!"
        except:
            pass

        if error is None:
             amount = course.price*100
             currency = "INR"
             reciept = f"Prodigyy-(int(time()))"
             notes = {"email" : user.email,
                      "name" : f'{user.first_name} {user.last_name}'
                     }
             order = client.order.create({'receipt' : reciept,
                                          'amount' : amount,
                                          'currency' : currency,
                                          'notes' : notes})
             payment = Payment()
             payment.user = user
             payment.course = course
             payment.order_id = order.get('id')
             payment.save()

    context = {
        "course": course,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error
        }
    return render(request, template_name="courses/checkout.html", context=context)


@csrf_exempt
def verifypayment(request):
    if request.method == "POST":
        data = request.POST
        context ={}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user = payment.user, course = payment.course)
            userCourse.save()

            payment.user_course = userCourse
            payment.save()
            return redirect("courses")
        except:
            return HttpResponse("invalid payment details")
