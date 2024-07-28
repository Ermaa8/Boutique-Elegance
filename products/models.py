from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        if self.category and self.category.discount_percentage:
            discount = (self.price * self.category.discount_percentage) / 100
            return self.price - discount
        return self.price


class OutfitCategory(models.Model):
    name = models.CharField(max_length=254)
    discount_value = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Discount value in percentage

    def __str__(self):
        return self.name


class Outfit(Product):
    outfit_category = models.ForeignKey(OutfitCategory, on_delete=models.CASCADE, null=True)  # Updated to use OutfitCategory
    products = models.ManyToManyField(Product, related_name="product_list", null=True)

    def __str__(self):
        return self.name

    def get_total_price(self):
        total = sum(product.get_discounted_price() for product in self.products.all())
        if self.category.discount_value:
            total -= (total * self.category.discount_value) / 100
        return total
