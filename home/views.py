from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.core import management
import datetime
from dateutil import relativedelta
from home.forms import CreateForm
from home.models import Funcionario, Documento
from django.contrib import messages


class HomeView(View):
    template_name = 'home/home_form.html'
    success_url = reverse_lazy('home:home')

    def get(self, request, pk=None):
        form = CreateForm()
        func = Funcionario.objects.all()
        # grafico pie
        contHome = Funcionario.objects.select_related('tipo_contrato').filter(
            tipo_contrato__tipo_contrato="home office").count()
        contInd = Funcionario.objects.select_related('tipo_contrato').filter(
            tipo_contrato__tipo_contrato="indeterminado").count()
        contExp = Funcionario.objects.select_related('tipo_contrato').filter(
            tipo_contrato__tipo_contrato="experiência").count()
        # grafico pie
        # grafico bar
        # Faixa etaria 1- '18-25 / 2- '26-35' / 3- '36-45' / 4 - '46-55' / 5- 'acima55'
        fEtaria = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}
        for f in func:
            # diferenca de data entre data nascimento e agora
            difDias = relativedelta.relativedelta(f.data_nascimento, datetime.datetime.now())
            if f.data_nascimento:
                difAnos = difDias.years.__abs__()
                if difAnos < 18:
                    continue
                elif difAnos >= 18 and difAnos <= 25:
                    fEtaria['f1'] += 1
                elif difAnos >= 26 and difAnos <= 35:
                    fEtaria['f2'] += 1
                elif difAnos >= 36 and difAnos <= 45:
                    fEtaria['f3'] += 1
                elif difAnos >= 46 and difAnos <= 55:
                    fEtaria['f4'] += 1
                else:
                    fEtaria['f5'] += 1
        # grafico bar

        ctx = {'form': form, 'func': func, 'contHome': contHome, 'contInd': contInd, 'contExp': contExp,
               'fEtaria': fEtaria}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        if form.is_valid():

            # salvar arquivo em media/home/Funcionarios.csv
            documento = Documento(documento=request.FILES['file'])
            documento.save()

            try:
                # executando python3 manage.py runscript csv_load
                management.call_command('runscript', 'csv_load')
            except:
                return HttpResponse("Erro ao inserir dados do CSV, contate o administrador.")

        # MSG de resposta para o sucesso do POST
        messages.success(self.request, 'Dados inseridos com sucesso')
        return HttpResponseRedirect(self.request.path_info)

