from django.contrib import admin
from .models import *
@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'kitob_soni', 'kurs', 'bitiruvchi')
    list_editable = ('kitob_soni', 'kurs', 'bitiruvchi')
    list_display_links = ('ism',)
    list_filter = ('bitiruvchi','kurs')
    search_fields = ('ism', 'id','kitob_soni')
    list_per_page = 7

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'kitob_soni', 'tirik')
    list_editable = ('kitob_soni', 'tirik')
    list_display_links = ('id', 'ism',)
    search_fields = ('ism', )
    list_filter = ('tirik',)

@admin.register(kitob)
class kitobAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'sahifa', 'janr', 'muallif')
    list_editable = ('sahifa',)
    list_display_links = ('nom', 'janr')
    search_fields = ('nom','id')
    list_filter = ('janr',)
    autocomplete_fields = ('muallif',)
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('ism','ish_vaqti')
    list_filter = ('ish_vaqti',)
    search_fields = ('ism',)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('talaba', 'kitob',)
    autocomplete_fields = ('talaba','kitob','admin')

