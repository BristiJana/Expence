from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(account)
admin.site.register(category)
admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(Bank)