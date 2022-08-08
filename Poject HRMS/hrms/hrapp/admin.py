from django.contrib import admin
from .models import Enquiry,Registration,AdminLogin


# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Registration)
admin.site.register(AdminLogin)
