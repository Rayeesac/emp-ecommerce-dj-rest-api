from django.db import models
import random
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Employee(models.Model):

    EMPLOYMENT_STATUS_CHOICES = [
        ("Active", "Active"),
        ("Retired", "Retired"),
        ("Internship", "Internship"),
    ]

    full_name = models.CharField(_("Full Name"), max_length=255)
    job_title = models.CharField(_("Job Title"), max_length=255, null=True, blank=True)
    employment_status = models.CharField(_("Employment Status"), max_length=50, null=True, blank=True, choices=EMPLOYMENT_STATUS_CHOICES)
    sub_unit = models.CharField(_("Sub Unit"), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.full_name}"

    def save(self, *args, **kwargs):

        # If not Job Title set a dummy value
        if not self.job_title:
            self.job_title = "Teacher"

        # If not Employment Status choose randomly
        if not self.employment_status:
            self.employment_status = random.choice(
                [status[0] for status in self.EMPLOYMENT_STATUS_CHOICES] 
            )

        # If not Sub Unit choose randomly
        if not self.sub_unit:
            if self.employment_status == "Active":
                self.sub_unit = "Accounting"
            elif self.employment_status == "Internship":
                self.sub_unit = "Sales"

        super().save(*args, **kwargs)

class Product(models.Model):
    sku = models.CharField(_("Product SKU"), max_length=255, unique=True, db_index=True)
    name = models.CharField(_("Product Name"), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    datetime = models.DateTimeField(_("Order Date"), default=timezone.now)
    products = models.ManyToManyField(Product, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quantity"), default=1, blank=True,null=True)