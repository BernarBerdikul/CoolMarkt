from django.contrib import admin
from .models import Bb, Rubric, UserMessage


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'subject', 'message')
    list_display_links = ('email', 'subject')
    search_fields = ('user_name', 'email', 'subject',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(UserMessage, UserMessageAdmin)




