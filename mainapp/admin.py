from django.contrib import admin

from mainapp.models import Question, Quiz


# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
