from django.contrib import admin
from .models import Osoba,OkregWyborczy,Radny,Komisja,Funkcja,SkladRady,SkladKomisji
# Register your models here.

@admin.register(Osoba)
class DzielniaOsobaAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    # prepopulated_fields = { 'slug': ('wspolnota',), }
    list_display = ['osobaId','nazwa','imie','nazwisko','email','tel','www','img_path']

@admin.register(Komisja)
class DzielniaKomisjaAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    prepopulated_fields = { 'slug': ('nazwaKomisji',), }
    list_display = ['komisjaId','nazwaKomisji','slug','przedmiot_dzialania','zadania','dzien','godzina']


@admin.register(OkregWyborczy)
class DzielniaOkregWyborczyAdmin(admin.ModelAdmin):
    list_display = ['okregId','nrOkregu','okreg']


@admin.register(Funkcja)
class DzielniaFunkcjaAdmin(admin.ModelAdmin):
    list_display = ['funkcjaId','nazwa','typ_funkcji','opis_typ']



@admin.register(SkladKomisji)
class DzielniaSkladKomisjiAdmin(admin.ModelAdmin):
    list_display = ['skladkomisjiId','komisjaId','radnyId','funkcjaId']



@admin.register(SkladRady)
class DzielniaSkladRadyAdmin(admin.ModelAdmin):
    list_display = ['skladRadyId','radnyId','funkcjaId']


@admin.register(Radny)
class DzielniaRadnyAdmin(admin.ModelAdmin):
    list_display = ['radnyId','osobaId','okregId']

