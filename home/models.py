from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class TipoContrato(models.Model):
    tipo_contrato = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.id} - {self.tipo_contrato}"


class Setor(models.Model):
    setor = models.CharField(max_length=5, null=False)

    def __str__(self):
        return f"{self.id} - {self.setor}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=20, null=False)
    data_nascimento = models.DateField(null=False)
    tipo_contrato = models.ForeignKey("TipoContrato", on_delete=models.CASCADE, related_name="contrato", null=False)
    setor = models.ForeignKey("Setor", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.id} - {self.nome}"


class OverwriteStorage(FileSystemStorage):
    '''
    Muda o comportamento padrão do Django e o faz sobrescrever arquivos de
    mesmo nome que foram carregados pelo usuário ao invés de renomeá-los.
    '''
    def get_available_name(self, nome='Funcionarios', max_length=30):
        if self.exists(nome):
            os.remove(os.path.join(settings.MEDIA_ROOT, nome))
        return nome

class Documento(models.Model):
    nome = models.CharField(max_length=30, default='Funcionarios')
    documento = models.FileField(upload_to='home/', storage=OverwriteStorage())
    data_upload = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.data_upload}"
