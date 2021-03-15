from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Turn(models.Model):
    nombre = models.CharField(max_length=120)

    class Reason(models.TextChoices):
        CONSULT = "CN", _("Consulta")
        OTHER = "OT", _("Otro")

    motivo = models.CharField(
        max_length=2,
        choices=Reason.choices,
        # default=Reason.CONSULT,
    )

    def is_upperclass(self):
        return self.motivo in {
            self.Reason.CONSULT,
            self.Reason.OTHER,
        }

    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
