from django.contrib import admin
from .models import CustomUser


class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    # fields = ('username','id',)
    list_display_links = ('username','email')
    list_display = ('id','username','email')
    list_filter = ('id',)
    list_per_page = 15
    search_fields = ('id', 'username')

admin.site.register(CustomUser, UserModelAdmin)

admin.site.site_title='Адиин панел'