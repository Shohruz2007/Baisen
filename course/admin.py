from django.contrib import admin
from parler.admin import TranslatableAdmin
import functools
from django.core.paginator import Paginator
from django.db import connection, transaction, OperationalError

from .models import *


class CourseAdmin(TranslatableAdmin):
    list_display = ('name','description',)
    readonly_fields = ('time_create','time_update','user','id')
    fieldsets = (
        (None, {
            'fields': ('id','name','description','price','planned_time','time_create','time_update','course_type','user','image',),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)


class CourseTypeAdmin(TranslatableAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id','name',),
        }),
    )

class CourseDataCategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id','name','course',),
        }),
    )

class CourseDataSubCategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id','name','category',),
        }),
    )

class CourseDataThemeAdmin(TranslatableAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id','name','content','image','video','links', 'extra_data', 'subcategory',),
        }),
    )

class CourseThemeTaskAdmin(TranslatableAdmin):
    list_display = ('content',)
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('id','content','course_theme','image',),
        }),
    )

class CourseThemeCommentAdmin(TranslatableAdmin):
    list_display = ('user','text',)
    readonly_fields = ('id','user',)
    fieldsets = (
        (None, {
            'fields': ('id','image','text','subcomment',),
        }),
    )
        
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)
        
        
class RegisterCourseUserAdmin(TranslatableAdmin):
    list_display = ('user',)
    readonly_fields = ('id','user',)
    fieldsets = (
        (None, {
            'fields': ('id' ,'course','time_create','time_update','is_finished','total_mark','proposed_time','completed_themes','is_manager',),
        }),
    )
        
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDataCategory, CourseDataCategoryAdmin)
admin.site.register(CourseDataSubCategory, CourseDataSubCategoryAdmin)
admin.site.register(CourseDataTheme, CourseDataThemeAdmin)
admin.site.register(CourseThemeComment, CourseThemeCommentAdmin)
admin.site.register(CourseThemeTask, CourseThemeTaskAdmin)
admin.site.register(RegisterCourseUser, )
admin.site.register(CourseType, CourseTypeAdmin)
