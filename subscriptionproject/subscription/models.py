from django.db import models
from django.urls import reverse

class Subscription(models.Model):
    email = models.EmailField(("Enter your email"), max_length=254)

    class Meta:
        verbose_name = ("Subscription")
        verbose_name_plural = ("Subscriptions")

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})