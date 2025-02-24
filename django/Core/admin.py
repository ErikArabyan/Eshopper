from django.contrib import admin
from .models import *
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.register(Contact)
admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Product)
admin.site.register(Circle)


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

# admin.site.register(CustomUser, CustomUserAdmin)