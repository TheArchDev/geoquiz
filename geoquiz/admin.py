from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Quiz, Country, UserProfile

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Country)
admin.site.register(UserProfile)