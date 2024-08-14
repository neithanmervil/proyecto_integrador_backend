from django.db import models

# Create your models here.


class Dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_dispositivo = models.CharField(max_length=255)
    descripcion = models.TextField()
    esta_disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'dispositivos_info'

    def __str__(self):
        return self.nombre_dispositivo

class Prestamo(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    telefono_estudiante = models.CharField(max_length=15)
    dispositivo = models.ForeignKey(Dispositivo, related_name='prestamos', on_delete=models.CASCADE, null=True, blank=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    
    class Meta:
        db_table = 'prestamos_info'    

    def __str__(self):
        return f'{self.nombre_estudiante} - {self.dispositivo}'
