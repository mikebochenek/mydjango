from django.contrib import admin
from .models import User, Dataset, Visualization

admin.site.register(User)
admin.site.register(Dataset)
admin.site.register(Visualization)
