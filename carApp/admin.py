from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Engine)
admin.site.register(Cars)
admin.site.register(Manufacturer)
admin.site.register(Feature)

