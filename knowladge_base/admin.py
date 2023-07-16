from django.contrib import admin
from .models import BaseTheme, KnowladgeBase
from parler.admin import TranslatableAdmin
import functools
from django.core.paginator import Paginator
from django.db import connection, transaction, OperationalError

class TimeLimitedPaginator(Paginator):
    """
    Paginator that enforces a timeout on the count operation.
    If the operations times out, a fake bogus value is
    returned instead.
    """
    @functools.cached_property
    def count(self):
        # We set the timeout in a db transaction to prevent it from
        # affecting other transactions.
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute('SET LOCAL statement_timeout TO 200;')
            try:
                return super().count
            except OperationalError:
                return 9999999999

class BaseThemeAdmin(TranslatableAdmin):
    list_display = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
    )

class KnowladgeBaseAdmin(TranslatableAdmin):
    list_display = ('name', 'description',)
    readonly_fields = ('id','time_create','time_update','author',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'image', 'link', 'theme', 'author', 'time_create', 'time_update', 'id',),
        }),
    )
    paginator =TimeLimitedPaginator

    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


admin.site.register(BaseTheme, BaseThemeAdmin)
admin.site.register(KnowladgeBase, KnowladgeBaseAdmin)
