from django.contrib import admin
from .models import Class

from icecream import ic
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk',)
    search_fields = ('pk', 'name')
    list_editable = ('name',)
    pass



admin.site.register(Class, ClassAdmin)

# admin.site.register(Classroom, ClassroomAdmin)

