from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from core.models import Payment
from django.contrib import messages



def homepage(request):
    all_categories = Category.objects.all()
    male_products = Product.objects.filter(category = 2)
    female_products = Product.objects.filter(category = 1)
    context = {'all_categories': all_categories,
               'male_products': male_products, 'female_products': female_products}
    return render(request, 'Store/index.html', context)

def singlepage(request, id):
    singleproduct = Product.objects.get(id=id)
    category = singleproduct.category
    other_products = Product.objects.filter(category=category).exclude(id=id)[:4]
    context = {"singleproduct": singleproduct, "other_products" : other_products}
    return render(request,'Store/single-product.html', context)

def initiate_payment(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        email = request.user.email
        amount = product.price
        payment = Payment.objects.create(email=email, amount=amount)
        context = {"payment": payment, "product": product}
        return render (request, "core/make_payment.html", context)
    context = {"product": product}
    return render (request, "Store/initiate_payment.html", context)



# def initiate_payment(request):
#     if request.method == "POST":
#         pay_form = Paymentform(request.POST)
#         if pay_form.is_valid():
#             payment = pay_form.save()
#             paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
#             return render(request, "core/make_payment.html", {'payment': payment, 'paystack_public_key': paystack_public_key})
#     else:
#         pay_form = Paymentform()
#     return render(request, "core/initiate_payment.html", {"pay_form": pay_form})


# def verify_payment(request, ref):
#     payment = get_object_or_404(Payment, ref=ref)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, "Verification Successful")
#     else:
#         messages.error(request, "Verification Failed")
#     return redirect("initiate_payment")