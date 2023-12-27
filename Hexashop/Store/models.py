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
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name