from django.contrib import admin

# import models from models module
from .models import Questions, Choice

# change the default header and title of admin page
admin.site.site_header = 'Pollapp Admin'
admin.site.site_title = 'Pollsapp Admin Area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':
            ['collapse']}),
    ]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Questions, QuestionAdmin)

# admin.site.register(Questions)
# admin.site.register(Choice)
