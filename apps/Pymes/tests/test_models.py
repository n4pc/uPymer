from django.test import TestCase
from apps.Pymes.models import Cat
import tempfile

class CatTestCase(TestCase):
    def setUp(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        Cat.objects.create(nombre="AAA", descripcion="descripcion 1", img=image)
        Cat.objects.create(nombre="BBB", descripcion="descripcion 2", img=image)

    def test_ingresar_pymes(self):
        """Las carreras se registran correctamente en la BD"""
        cat_1 = Cat.objects.get(nombre="AAA")
        cat_2 = Cat.objects.get(nombre="BBB")
        self.assertEqual(cat_1.descripcion, "descripcion 1")
        self.assertEqual(cat_2.descripcion, "descripcion 2")
