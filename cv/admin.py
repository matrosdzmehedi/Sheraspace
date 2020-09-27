from django.contrib.auth.models import Group
from django.contrib import admin
from .models import PersonCv


class PersonCvAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'phone')
    prepopulated_fields = {'slug': ('name',)}


admin.site.unregister(Group)
admin.site.register(PersonCv, PersonCvAdmin)
