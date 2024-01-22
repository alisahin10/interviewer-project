from django.contrib import admin
from .models import Question, Category, Test

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "slug")
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description")
    list_filter = ("category", "is_active", "is_home")

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Test)
