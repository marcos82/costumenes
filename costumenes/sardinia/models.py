import os
import uuid


from imagekit.models import ImageSpecField
from imagekit.processors import Crop


from django.db import models

# A list of sardinian's regions
SARDINIA_REGIONS = (
    (u'Anglona', u'Anglona'),
    (u'Barbagia', u'Barbagia'),
    (u'Baronia', u'Baronia'),
    (u'Campidano', u'Campidano'),
    (u'Gallura', u'Gallura'),
    (u'Gerrei', u'Gerrei'),
    (u'Goceano', u'Goceano'),
    (u'Iglesiente', u'Iglesiente'),
    (u'Logudoro', u'Logudoro'),
    (u'Mandrolisai', u'Mandrolisai'),
    (u'Marghine', u'Marghine'),
    (u'Marmilla', u'Marmilla'),
    (u'Meilogu', u'Meilogu'),
    (u'Montacuto', u'Montacuto'),
    (u'Nurra', u'Nurra'),
    (u'Ogliastra', u'Ogliastra'),
    (u'Planargia', u'Planargia'),
    (u'Romangia', u'Romangia'),
    (u'Sarcidano', u'Sarcidano'),
    (u'Sarrabus', u'Sarrabus'),
    (u'Sassarese', u'Sassarese'),
    (u'Sulcis', u'Sulcis'),
    (u'Trexenta', u'Trexenta'),
)

# A list of sardinian's provinces
SARDINIA_PROVINCES = (
    (u'CA', u'Provincia di Cagliari'),
    (u'NU', u'Provincia di Nuoro'),
    (u'OR', u'Provincia di Oristano'),
    (u'SS', u'Provincia di Sassari'),
)

SI_NO = (
    (u'Si', u'SI'),
    (u'No', u'NO'),
)

COSTUME_SEX = (
    (u'Maschile', u'Costume maschile'),
    (u'Femminile', u'Costume femminile'),
)

COSTUME_TIPOLOGY = (
    (u'Vedova', u'Costume femminile da vedova'),
    (u'Sposa', u'Costume femminile da sposa'),
    (u'Femminile_quotidiano', u'Costume femminile di tutti i giorni'),
    (u'Maschile_quotidiano', u'Costume maschile di tutti i giorni'),
)

#This function will return the path based on the "comune" and "costume" value
def original_directory_generator(instance, path):
    return 'photos/%s/%s/%s.jpg' %(instance.comune.nome.lower(), instance.tipologia.lower(), uuid.uuid4())

def original_directory_generator_thumb(instance, path, specname, extension):
    return 'photos/%s/%s/%s' %(instance.comune.nome.lower(), instance.tipologia.lower(), os.path.basename(instance.img.name))


class Comune(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    regione = models.CharField(max_length=50, choices=SARDINIA_REGIONS)
    provincia = models.CharField(max_length=2, choices=SARDINIA_PROVINCES)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "comuni"

class Photo(models.Model):
    comune = models.ForeignKey(Comune)
    sesso = models.CharField(max_length=20, choices=COSTUME_SEX)
    tipologia = models.CharField(max_length=50, choices=COSTUME_TIPOLOGY)

    img = models.ImageField("path immagine", upload_to=original_directory_generator)
    # the thumbnail is not saved, it's cropped at runtime. Check if it can be slower with many images
    thumbnail = ImageSpecField(processors=[Crop(100, 50)], image_field='img', format='JPEG',
                               options={'quality': 90}, cache_to=original_directory_generator_thumb)

    num_views = models.PositiveIntegerField(editable=False, default=0)
    titolo = models.CharField(max_length=100)


    descrizione = models.TextField()
    data_scatto = models.DateTimeField()
    data_inserimento = models.DateTimeField(auto_now_add=True)
    autore_scatto = models.CharField(max_length=100, null=True, blank=True)
    localita_scatto = models.CharField(max_length=150, null=True, blank=True)
    nome_cognome_modello = models.CharField(max_length=100, null=True, blank=True)
    foto_copertina = models.CharField(max_length=2, choices=SI_NO, default="No")

    def __unicode__(self):
        return "%s - %s - %s" % (self.comune, self.tipologia.replace("_", " "), self.titolo)

    class Meta:
        verbose_name_plural = "foto"

"""
Definisce una categoria da associare al model gallery di foto.
La categoria permette di definire il numero max di foto da presentare nella gallery.
Le foto tipicamente sono ciclate mediante script javascript, percui se il limite max di foto e'
per esempio 3, e si caricano in tutto 5 immagini, le restanti 2 verrano visualizzate
al secondo ciclo
"""
class Category(models.Model):
    nome_category = models.CharField(max_length=255)
    max_photo = models.IntegerField()

    def __unicode__(self):
        return '%s - %s' % (self.nome_category, self.max_photo)

    class Meta:
        verbose_name_plural = 'categorie'

"""
Definisce una gallery di foto (da mostrare per esempio nella home page ecc)
Ciascuna gallery ha una categoria di appartenenza
"""
class Gallery(models.Model):
    nome_gallery = models.CharField(max_length=255)
    img = models.ImageField("path immagine", upload_to="foto_gallery")
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s - %s' % (self.nome_gallery, self.categoria.nome_category)

    class Meta:
        verbose_name_plural = 'gallery'

