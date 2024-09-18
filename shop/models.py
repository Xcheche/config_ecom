from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    title = models.CharField(max_length=255)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    category = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.ImageField(
        upload_to="product_images/", default="product_images/default.png"
    )

    def clean(self):
        if self.discount_price and self.discount_price >= self.price:
            raise ValidationError(
                "Discount price must be lower than the original price."
            )

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ["title"]

    def __str__(self):
        return self.title
