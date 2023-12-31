# Generated by Django 4.2.7 on 2023-11-08 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TipoContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.setor')),
                ('tipo_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipocontrato')),
            ],
        ),
    ]
