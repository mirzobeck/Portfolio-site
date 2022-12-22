from django.contrib import admin
from .models import about, work, skill, contact
# Register your models here.


admin.site.register(about)
admin.site.register(work)
admin.site.register(skill)
admin.site.register(contact)