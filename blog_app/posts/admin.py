from django.contrib import admin
from posts.models import Auther , Content
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class AutherAdmin(admin.ModelAdmin):
    list_display = ['name','topic','pub_date']
    list_filter = ['pub_date']
    search_fields = ['topic']
    inlines = [ContentInline]
    class Media:
        js = ('js/admin/place.js',)





admin.site.register(Auther, AutherAdmin)
admin.site.register(Content)