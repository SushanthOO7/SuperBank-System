from django.contrib import admin
from .models import Customers, Transactions
# Register your models here.
admin.site.register(Customers)
admin.site.register(Transactions)