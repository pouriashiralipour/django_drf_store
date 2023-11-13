from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("title"))
    description = models.CharField(
        max_length=500, blank=True, verbose_name=_("description")
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("datetime_created")
    )


class Discount(models.Model):
    discount = models.FloatField(verbose_name=_("discount"))
    description = models.CharField(max_length=250, verbose_name=_("description"))


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name=_("name"))
    slug = models.SlugField(verbose_name=_("slug"))
    description = models.TextField(verbose_name=_("description"))
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name=_("category")
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("price"))
    discounts = models.ManyToManyField(
        Discount, blank=True, verbose_name=_("discounts")
    )
    inventory = models.PositiveIntegerField(verbose_name=_("inventory"))
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("datetime_created")
    )
    datetime_modified = models.DateTimeField(
        auto_now=True, verbose_name=_("datetime_modified")
    )


class Customer(models.Model):
    fisrt_name = models.CharField(max_length=250, verbose_name=_("fisrt_name"))
    last_name = models.CharField(max_length=250, verbose_name=_("last_name"))
    email = models.EmailField(verbose_name=_("email"))
    phone_number = models.CharField(max_length=15, verbose_name=_("phone_number"))
    birth_day = models.DateField(null=True, blank=True, verbose_name=_("birth_day"))


class Address(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True, verbose_name=_("customer")
    )
    province = models.CharField(max_length=250, verbose_name=_("province"))
    city = models.CharField(max_length=250, verbose_name=_("city"))
    street = models.CharField(max_length=255, verbose_name=_("street"))


class Order(models.Model):
    ORDER_STATUS_PAID = "p"
    ORDER_STATUS_UNPAID = "u"
    ORDER_STATUS_CANCELED = "c"
    ORDER_STATUS = [
        (ORDER_STATUS_PAID, "Paid"),
        (ORDER_STATUS_UNPAID, "Unpaid"),
        (ORDER_STATUS_CANCELED, "Canceled"),
    ]
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name=_("customer")
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("datetime_created")
    )
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS,
        default=ORDER_STATUS_UNPAID,
        verbose_name=_("status"),
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
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product")
    )
    name = models.CharField(max_length=250, verbose_name=_("name"))
    body = models.TextField(verbose_name=_("body"))
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("datetime_created")
    )
    status = models.CharField(
        max_length=1,
        choices=COMMENT_STATUS,
        default=COMMENT_STATUS_WAITING,
        verbose_name=_("status"),
    )
