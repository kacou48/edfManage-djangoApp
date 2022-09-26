from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date',)
    prepopulated_fields = {'slug': ('titre', ),}


admin.site.register(Formation)
admin.site.register(Contact)
admin.site.register(Blog, PostAdmin)
admin.site.register(FacturationMensuelle)
admin.site.register(Feedback)

