from django.contrib import admin
from .models import Departments, Doctors

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Departments, DepartmentAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doc_name','departments','available']
    list_editable = ['available']
    

admin.site.register(Doctors,DoctorAdmin)    