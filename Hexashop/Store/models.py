from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_image')
    description = models.TextField(blank = True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name
    


class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length = 100)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"payment {self.amount}"
    def amount_value(self):
        return self.amount * 100
    
    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            if not Payment.objects.filter(ref=ref).exists():
                self.ref = ref
        super().save(*args, **kwargs)

    def verify_payment(self):
        payment = PayStack()
        status, result = payment.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
    