from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class FileModel(models.Model):
    name = models.CharField(max_length=100)
    files = models.FileField(upload_to='files__', validators=[FileExtensionValidator(['pdf', 'png', 'jpg'])])

    def __str__(self) -> str:
        return self.name