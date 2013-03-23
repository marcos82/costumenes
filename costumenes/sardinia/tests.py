from datetime import datetime
from django.test import TestCase
from django.test.client import Client
from sardinia.models import Comune, Photo

class SardiniaViewTest(TestCase):

    def test_get_regioni(self):
        c = Client()
        response = c.get('/costumenes/regioni/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '["Anglona", "Barbagia", "Baronia", "Campidano", "Gallura", "Gerrei", "Goceano",'
                                            ' "Iglesiente", "Logudoro", "Mandrolisai", "Marghine", "Marmilla", "Meilogu", '
                                            '"Montacuto", "Nurra", "Ogliastra", "Planargia", "Romangia", "Sarcidano", "Sarrabus", '
                                            '"Sassarese", "Sulcis", "Trexenta"]')

    def test_get_province(self):
        c = Client()
        response = c.get('/costumenes/province/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '["CA", "NU", "OR", "SS"]')

    def test_get_comuni(self):
        #creating a comune for test

        comune = Comune(nome='Testname', descrizione='Description', regione='Barbagia', provincia='Nu')
        comune.save()

        c = Client()
        response = c.get('/costumenes/comuni/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[]')

        #Creates a photo and associate it to the comune
        photo = Photo(comune=comune, sesso='Maschile', tipologia='Maschile_quotidiano', img='', titolo='Test',
                      data_scatto=datetime.today())
        photo.save()
        c = Client()
        response = c.get('/costumenes/comuni/')
        self.assertNotEqual(response.content, '[]')