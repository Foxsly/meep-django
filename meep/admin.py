from meep.models import Message, Topic, User
from django.contrib import admin

__author__ = 'Tim'

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author Stuff', {'fields': ['author'], 'classes': ['collapse']}),
        ('Topic Information', {'fields': ['title']})
    ]
    inlines = [MessageInline]
    list_display = ('title', 'author')

admin.site.register(Topic, TopicAdmin)
#admin.site.register(Message)
admin.site.register(User)