from django.shortcuts import render, redirect, get_object_or_404
from .forms import Paymentform
from django.contrib import messages
from .models import Payment
from django.conf import settings

# Create your views here.

def initiate_payment(request):
    if request.method == "POST":
        pay_form = Paymentform(request.POST)
        if pay_form.is_valid():
            payment = pay_form.save()
            paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
            return render(request, "core/make_payment.html", {'payment': payment, 'paystack_public_key': paystack_public_key})
    else:
        pay_form = Paymentform()
    return render(request, "core/initiate_payment.html", {"pay_form": pay_form})





# def verify_payment(request, ref):
#     payment = get_object_or_404(Payment, ref=ref)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, "Verification Successful")
#     else:
#         messages.error(request, "Verification Failed")
#     return redirect("initiate_payment")