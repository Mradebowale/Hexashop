from django.urls import path
from .views import homepage, singlepage, initiate_payment

urlpatterns = [
    path('', homepage, name="home"),
    path("single/<int:id>/", singlepage, name="detailpage"),
    path("single<int:id>/pay/", initiate_payment, name="" )
]
