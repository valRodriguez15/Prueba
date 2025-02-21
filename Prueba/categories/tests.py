from django.test import TestCase
from categories.models import Tours, Activities
from users.models import User

#Prueba de verificacion de la categoria Tours, con los campos que se declararon
class ToursTest(TestCase):
    #Metodo setUp se ejecuta antes de cada prueba y se envian los datos de prueba
    def setUp(self):
        self.user = User.objects.create(username='usuarioPrueba', email='prueba@tour.com')
        self.tour = Tours.objects.create(
            nombre='Tour de Prueba',
            descripcion='Descripción del tour de prueba.',
            precio=100000.00,
            disponibilidad=True,
            ubicacion='Ubicación de prueba',
            user=self.user
        )
    #la prueba verifica que se haya creado correctamente el modelo de Tours
    def test_new_tour(self):
        self.assertEqual(self.tour.nombre, 'Tour de Prueba')
        self.assertEqual(self.tour.user.username, 'usuarioPrueba')

#Prueba de verificacion de la categoria Actividades, con los campos que se declararon
class ActivitiesTest(TestCase):
    def setUp(self):
        self.tour = Tours.objects.create(
            nombre='Tour de Prueba',
            descripcion='Descripción del tour de prueba.',
            precio=100000.00,
            disponibilidad=True,
            ubicacion='Ubicación de prueba',
            user=None
        )
        self.activity = Activities.objects.create(
            nombre='Actividad de Prueba',
            detalle='Detalle de la actividad de prueba.',
            precio=50000.00,
            horario='10:00 AM - 5:00 PM',
            edadMin='10 años',
            tour=self.tour
        )

    def test_new_activity(self):
        self.assertEqual(self.activity.nombre, 'Actividad de Prueba')
        self.assertEqual(self.activity.tour.nombre, 'Tour de Prueba')
