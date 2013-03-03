from django.test import TestCase
from django.test.client import Client



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