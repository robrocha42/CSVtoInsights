import csv  # https://docs.python.org/3/library/csv.html
from datetime import datetime

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# comando para rodar script
# python3 manage.py runscript csv_load

from home.models import TipoContrato, Setor, Funcionario

# 'UTF-8' para reconhecer e salvar caracteres
def run():
    fhand = open('media/home/Funcionarios.csv', encoding='UTF-8')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    # deletar tudo do banco
    #TipoContrato.objects.all().delete()
    #Setor.objects.all().delete()
    #Funcionario.objects.all().delete()
    #Documento.objects.all().delete()

    # Formato do CSV
    # Nome, CPF, Data de nascimento, Tipo de contrato, Setor

    for row in reader:
        #print(row)

        # insert/save nas tabelas que têm relacionamento com o Funcionario - created será true or false
        tcon, created = TipoContrato.objects.get_or_create(tipo_contrato=row[3].strip())
        set, created = Setor.objects.get_or_create(setor=row[4].strip())

        # salvar no formato necessario YYYY-MM-DD
        d_nasc = row[2].strip()
        d = datetime.strptime(d_nasc, '%d/%m/%Y')
        d.strftime('%Y/%m/%d')

        #try:
        #    y = int(row[3])
        #except:
        #    y = None

        # insert/save no Funcionario - Dados do csv com suas respectivas chaves estrangeiras (TipoContrato, Setor)
        func = Funcionario(nome=row[0].strip(), cpf=row[1].strip(), data_nascimento=d, tipo_contrato=tcon, setor=set)
        func.save()
