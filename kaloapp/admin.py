from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(item_model)
admin.site.register(login_model)
admin.site.register(school_model)
admin.site.register(itempoints_model)
admin.site.register(schoolpoint_model)

