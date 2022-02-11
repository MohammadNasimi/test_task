from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(Receipt)
admin.site.register(Off_code)
admin.site.register(Discount)