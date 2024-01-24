from django.contrib import admin
from .models import HotelInfo,Comment,ContactUs
# Register your models here.

admin.site.register(HotelInfo)
admin.site.register(Comment)
admin.site.register(ContactUs)