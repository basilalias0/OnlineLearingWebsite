from django.shortcuts import render
from courses.models import Course
from django.shortcuts import redirect
from Prodigyy.settings import KEY_ID,KEY_SECRET
from courses.models.payment import Payment
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
    payment = None
    if action == 'create_payment':
        amount = course.price
        currency = "INR"
        reciept = f"Prodigyy-(time())"
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
        "user": user
        }
    return render(request, template_name="courses/checkout.html",
                  context=context)
