from django.contrib import admin

# Register your models here.
from .models import *
# from .models import NodalOfficer, Invoice

admin.site.register(NodalOfficer)

admin.site.register(Invoice)
admin.site.register(Admin)
admin.site.register(Hearing)
admin.site.register(AddCases)
admin.site.register(Advocate)