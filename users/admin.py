from django.contrib import admin
from .models import Category, Books, User, Cart

admin.site.register([Category, Books])
admin.site.register(User)
admin.site.register(Cart)
