from django.contrib import admin
from .models import Question, Choice, Layout

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Layout)