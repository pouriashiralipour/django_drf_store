from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discounts = models.ManyToManyField(Discount, blank=True)
    inventory = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    fisrt_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    birth_day = models.DateField(null=True, blank=True)


class Address(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )
    province = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=255)


class Order(models.Model):
    ORDER_STATUS_PAID = "p"
    ORDER_STATUS_UNPAID = "u"
    ORDER_STATUS_CANCELED = "c"
    ORDER_STATUS = [
        (ORDER_STATUS_PAID, "Paid"),
        (ORDER_STATUS_UNPAID, "Unpaid"),
        (ORDER_STATUS_CANCELED, "Canceled"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID
    )


class Comment(models.Model):
    COMMENT_STATUS_WAITING = "w"
    COMMENT_STATUS_APPROVED = "a"
    COMMENT_STATUS_NOTAPRROVED = "na"
    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, "Wating"),
        (COMMENT_STATUS_APPROVED, "Approves"),
        (COMMENT_STATUS_NOTAPRROVED, "Not Approved"),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING
    )
