from django.contrib import admin
# import your models here
from .models import Car, Fueling, Driver

# Register your models here
admin.site.register(Car)

# register the new Fueling Model 
admin.site.register(Fueling)
admin.site.register(Driver)
