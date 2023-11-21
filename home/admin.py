from django.contrib import admin
from .models import TipoContrato, Setor, Funcionario, Documento

# Register your models here.
# aparecer no /admin
admin.site.register(TipoContrato)
admin.site.register(Setor)
admin.site.register(Funcionario)
admin.site.register(Documento)
