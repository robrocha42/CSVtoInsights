from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from humanize import naturalsize
from home.models import Documento
#from pprint import pprint


# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 1 * 2 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # algum model precisa ser especificado
    class Meta:
        model = Documento
        fields = []

    # validação tamanho do arquivo
    # Call this 'file' so it gets copied from the form to the in-memory model
    # file é o name do campo input
    file = forms.FileField(required=True, label='O arquivo deve ser menor que ou igual a '+max_upload_limit_text)
    upload_field_name = 'file'

    # metodo clean() para sobrescrever a validação
    def clean(self):
        cleaned_data = super().clean()
        fil = cleaned_data.get('file')
        if fil is None:
            return
        if len(fil) > self.max_upload_limit:
            self.add_error('file', "O arquivo deve ser menor que ou igual a "+self.max_upload_limit_text)
        if fil._name != 'Funcionarios.CSV' and fil._name != 'Funcionarios.csv':
            self.add_error('file', "O nome do arquivo deve ser igual a Funcionarios.CSV")


