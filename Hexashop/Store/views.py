from django.shortcuts import render
from .models import Category, Product
from core.models import Payment


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
        email = request.user
        amount = product.price
        payment = Payment.objects.create(email=email, amount=amount)
        context = {"payment": payment, "product": product}
        return render (request, "make_payment", context)
    context = {"product": product}
    return render (request, "Store/initiate_payment.html", context)