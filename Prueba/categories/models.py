from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import SET_NULL
from users.models import User

class Tours(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
        MinValueValidator(60000.00),
        MaxValueValidator(300000.00)
        ]
    )
    disponibilidad = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=200)
    #Usuario que creo el Tour, cuando se elimine no se borra, sino que queda User=null
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Activities(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    detalle = models.TextField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(20000.00),
            MaxValueValidator(90000.00)
        ]
    )
    horario = models.CharField(max_length=100)
    edadMin = models.CharField(max_length=30)
    miniature = models.ImageField(upload_to='categories/img/', null=True, blank=True)
    tour = models.ForeignKey(Tours, related_name='activities', on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        if self.tour and not self.tour.disponibilidad:
            raise ValidationError('La actividad solo puede ser agregada a tours disponibles.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
