from django.db import models

# Create your models here.

class Osoba(models.Model):
    osobaId=models.AutoField(primary_key=True)
    nazwa=models.CharField(max_length=350)
    imie=models.CharField(max_length=150)
    nazwisko=models.CharField(max_length=250)
    email=models.CharField(max_length=350,blank=True,null=True)
    tel=models.CharField(max_length=20,blank=True,null=True)
    www=models.CharField(max_length=3500,blank=True,null=True)
    img_path=models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return f'{self.osobaId} = {self.nazwa}'


class OkregWyborczy(models.Model):
    okregId=models.AutoField(primary_key=True)
    nrOkregu=models.IntegerField()
    okreg=models.CharField(max_length=3000)

    def __str__(self):
        return f'{self.nrOkregu} = {self.okreg}'


class Radny(models.Model):
    radnyId=models.AutoField(primary_key=True)
    osobaId=models.ForeignKey(Osoba,on_delete=models.CASCADE)
    okregId=models.ForeignKey(OkregWyborczy,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.osobaId}'


class Komisja(models.Model):
    komisjaId=models.AutoField(primary_key=True)
    nazwaKomisji=models.CharField(max_length=500,blank=True,null=True)
    slug=models.SlugField(max_length=500,null=True)
    przedmiot_dzialania=models.CharField(max_length=5000,blank=True,null=True)
    zadania=models.CharField(max_length=500,blank=True,null=True)
    dzien=models.DateField(auto_now=True,blank=True,null=True)
    godzina=models.TimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f'{self.komisjaId} {self.nazwaKomisji}'


class Funkcja(models.Model):
    class SkladTyp(models.IntegerChoices):
        Rada = 2
        Komisja = 1

    funkcjaId=models.AutoField(primary_key=True)
    nazwa=models.CharField(max_length=300,blank=True,null=True)
    typ_funkcji=models.IntegerField(choices=SkladTyp.choices)
    opis_typ=models.CharField(max_length=20)

    def __str__(self):
        return f' {self.funkcjaId} {self.nazwa} ({self.opis_typ})'


class SkladRady(models.Model):
    skladRadyId = models.AutoField(primary_key=True)
    radnyId = models.ForeignKey(Radny,on_delete=models.CASCADE)
    funkcjaId = models.ForeignKey(Funkcja,on_delete=models.CASCADE)

    def __str__(self):
        return f'SKŁAD RADY {self.radnyId}'


class SkladKomisji(models.Model):
    skladkomisjiId=models.AutoField(primary_key=True)
    komisjaId = models.ForeignKey(Komisja,on_delete=models.CASCADE)
    radnyId = models.ForeignKey(Radny,on_delete=models.CASCADE)
    funkcjaId = models.ForeignKey(Funkcja,on_delete=models.CASCADE)

    def __str__(self):
        return f'SKŁAD KOMISJI {self.komisjaId}'


